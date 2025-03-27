import os
import httpx


async def transcribe(audio_bytes: bytes) -> str:
    async with httpx.AsyncClient() as client:
        files = {"file": ("audio.wav", audio_bytes, "audio/wav")}
        data = {"model": "whisper-1"}
        headers = {"Authorization": f'Bearer {os.getenv("OPENAI_API_KEY")}'}
        response = await client.post(
            "https://api.openai.com/v1/audio/transcriptions",
            files=files,
            data=data,
            headers=headers,
        )
        response.raise_for_status()
        return response.json().get("text", "")
