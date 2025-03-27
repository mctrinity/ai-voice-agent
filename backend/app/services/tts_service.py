import httpx
import os


async def speak(text: str) -> str:
    voice_id = (
        "your_default_voice_id"  # You can fetch available voices via ElevenLabs API
    )
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        "Content-Type": "application/json",
    }
    json_data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=json_data)
        response.raise_for_status()

        # Save or stream audio
        audio_path = f"output/response_{hash(text)}.mp3"
        with open(audio_path, "wb") as f:
            f.write(response.content)

    return audio_path  # or return audio bytes
