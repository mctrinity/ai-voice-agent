# 🧠 AI Voice Agent Platform

An intelligent voice automation platform that combines Twilio (or SignalWire), OpenAI Whisper, GPT-4, ElevenLabs, and integrations like Google Calendar to create a smart, conversational phone agent.

---

## 🔥 Features

- ☎️ **Voice Call Management** using Twilio
- 🎧 **Speech-to-Text (STT)** with OpenAI Whisper
- 🧠 **Conversational Reasoning** via GPT-4 or Claude
- 🗣️ **Text-to-Speech (TTS)** using ElevenLabs
- 🗖️ **Calendar & Appointment Integration** (Google Calendar, Calendly, Fresha)
- 🧪 **Internal Tools** for testing and managing workflows
- 🛠️ **REST API** endpoints for frontend dashboard integration

---

## 🗂️ Project Structure

```
ai-voice-agent/
├── backend/
│   ├── app/
│   │   ├── api/               # FastAPI route handlers
│   │   ├── core/              # AI engine, config
│   │   ├── services/          # Twilio, GPT, Whisper, TTS
│   │   ├── models/            # Data models (call logs, etc.)
│   │   └── main.py            # FastAPI entry point
│   └── requirements.txt
├── .env                       # Environment variables
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ai-voice-agent.git
cd ai-voice-agent/backend
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure `.env`

Create a `.env` file in the root with your keys:

```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
OPENAI_API_KEY=sk-...
ELEVENLABS_API_KEY=...
GOOGLE_API_CREDENTIALS_PATH=secrets/google.json
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

---

## 📞 Example Call Flow

1. Caller dials a Twilio number
2. Twilio webhook hits `/calls/twilio/incoming`
3. Audio is transcribed via Whisper
4. GPT-4 generates a response
5. ElevenLabs converts text → voice
6. Twilio streams the response back to the caller

---

## 🧹 Stack

| Purpose      | Tech Used                 |
| ------------ | ------------------------- |
| Backend API  | FastAPI (Python)          |
| Telephony    | Twilio / SignalWire       |
| AI Reasoning | GPT-4 / Claude            |
| STT          | OpenAI Whisper            |
| TTS          | ElevenLabs                |
| Scheduling   | Google Calendar, Calendly |
| Deployment   | Railway, Render, Docker   |

---

## 📌 Roadmap

- [ ] Twilio integration with full webhook call flow
- [ ] AI response pipeline (Whisper → GPT → ElevenLabs)
- [ ] Google Calendar sync
- [ ] Internal admin/test dashboard
- [ ] Multi-agent context/memory support

---

## 🛡️ License

MIT License — free to use, modify, and distribute.

---

## 👋 Contributing

PRs welcome! Let's build voice AI that actually works in the real world.

---

## 💬 Questions?

Drop an issue or ping me [@yourusername](https://github.com/yourusername).
