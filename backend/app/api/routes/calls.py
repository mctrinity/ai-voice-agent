from fastapi import APIRouter, Request, UploadFile, File
from app.services.signalwire_service import handle_incoming_call
from app.services.whisper_service import transcribe
from app.services.gpt_service import respond
from fastapi.responses import StreamingResponse
from app.services.elevenlabs_service import text_to_speech
from app.core.config import settings

router = APIRouter()


@router.get("/config")
def get_config():
    return {"ngrok_base_url": settings.NGROK_BASE_URL}


@router.post("/signalwire/incoming")
async def signalwire_incoming(request: Request):
    body = await request.body()
    return await handle_incoming_call(body)


@router.get("/signalwire/incoming")
async def signalwire_get():
    return {"status": "This endpoint is live and reachable via GET."}


@router.post("/simulate/transcribe")
async def simulate_transcription(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    transcript = await transcribe(audio_bytes)
    return {"transcript": transcript}


@router.post("/simulate/ai-call")
async def simulate_ai_call(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    # 1. Transcribe
    transcript = await transcribe(audio_bytes)

    # 2. Get GPT response
    ai_response = await respond(transcript)

    # 3. Convert GPT response to speech using ElevenLabs
    audio_output = await text_to_speech(ai_response)

    # 4. Return audio file as stream
    return StreamingResponse(
        iter([audio_output]),
        media_type="audio/mpeg",
        headers={"Content-Disposition": "attachment; filename=ai-response.mp3"},
    )
