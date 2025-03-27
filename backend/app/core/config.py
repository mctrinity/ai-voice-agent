import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class Settings:
    # SignalWire Credentials
    SIGNALWIRE_PROJECT_ID = os.getenv("SIGNALWIRE_PROJECT_ID")
    SIGNALWIRE_API_TOKEN = os.getenv("SIGNALWIRE_API_TOKEN")
    SIGNALWIRE_SPACE_URL = os.getenv("SIGNALWIRE_SPACE_URL")
    SIGNALWIRE_PHONE_NUMBER = os.getenv("SIGNALWIRE_PHONE_NUMBER")

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # ElevenLabs
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

    # Google API (optional, for calendar later)
    GOOGLE_API_CREDENTIALS_PATH = os.getenv("GOOGLE_API_CREDENTIALS_PATH")


settings = Settings()
