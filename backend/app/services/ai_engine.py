from app.services import whisper_service, gpt_service, tts_service


async def process_audio(audio_bytes: bytes) -> str:
    transcript = await whisper_service.transcribe(audio_bytes)
    ai_response = await gpt_service.respond(transcript)
    audio_file_path = await tts_service.speak(ai_response)
    return audio_file_path
