import httpx
from app.core.config import settings

print("OpenAI API Key in runtime:", settings.OPENAI_API_KEY[:10], "...")  # Partial key


async def respond(transcript: str) -> str:
    prompt = f"You are a friendly voice assistant. A user said: '{transcript}'. What should you say back?"
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }
        json_data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": transcript},
            ],
        }
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
