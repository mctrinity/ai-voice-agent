import os
import httpx


async def text_to_speech(text: str) -> bytes:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel's voice ID

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print("❌ ElevenLabs error:", e.response.text)
            raise

        return response.content  # MP3 audio
