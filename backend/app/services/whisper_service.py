import os
import httpx


async def transcribe(audio_bytes: bytes) -> str:
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
    data = {"model": "whisper-1", "language": "en"}

    files = {"file": ("audio.wav", audio_bytes, "audio/wav")}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()
        return response.json()["text"]
