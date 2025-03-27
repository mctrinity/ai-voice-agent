from fastapi.responses import PlainTextResponse
from app.services.gpt_service import respond


async def handle_incoming_call(body: bytes):
    # Simulated transcript (replace with Whisper later)
    simulated_transcript = "Hi, I need help booking a haircut appointment."

    # Generate GPT response
    try:
        ai_response = await respond(simulated_transcript)
    except Exception as e:
        print("GPT Error:", e)
        ai_response = "Sorry, I'm having trouble responding right now."

    # Format SignalWire XML
    response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="female" language="en-US">
        {ai_response}
    </Say>
</Response>"""

    return PlainTextResponse(content=response, media_type="application/xml")
