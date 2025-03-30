import httpx
from datetime import datetime
from app.core.config import settings


async def respond(transcript: str) -> str:
    # Inject current time (optional)
    current_time = datetime.now().strftime("%A, %B %d at %I:%M %p")

    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }

        json_data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a friendly AI voice assistant. "
                        "Keep all responses under 2 sentences and suitable for voice output. Be concise."
                        f"The current time is {current_time}. "
                        "Avoid saying you don’t have real-time access. "
                        "Instead, respond helpfully or suggest possibilities."
                    ),
                },
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
