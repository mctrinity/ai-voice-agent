import os
import httpx


async def text_to_speech(text: str) -> bytes:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel's voice ID

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}

    # Optional: truncate text to 200 characters
    safe_text = text[:200]

    data = {
        "text": safe_text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=data, timeout=15.0)
            response.raise_for_status()
            return response.content  # MP3 audio
        except httpx.HTTPStatusError as e:
            print("❌ ElevenLabs error:", e.response.text)
            raise
        except httpx.ReadTimeout:
            print("⏱️ ElevenLabs timed out. Try shorter text or increase timeout.")
            raise
