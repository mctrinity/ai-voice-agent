# 🧠 AI Voice Agent Platform

An intelligent voice automation platform that combines **SignalWire**, OpenAI Whisper, GPT-4, ElevenLabs, and integrations like Google Calendar to create a smart, conversational phone agent.

---

## 🔥 Features

- ☎️ **Voice Call Management** using SignalWire
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
│   │   ├── core/              # Config settings
│   │   ├── services/          # SignalWire, Whisper, GPT, TTS, AI engine
│   │   ├── models/            # Data models (call logs, etc.)
│   │   ├── static/            # index.html (Web UI)
│   │   └── main.py            # FastAPI entry point
│   ├── .env                   # Environment variables
│   └── requirements.txt
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
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure `.env`

Create a `.env` file **inside the `backend/` folder** with your keys:

```env
SIGNALWIRE_PROJECT_ID=your_project_id
SIGNALWIRE_API_TOKEN=your_api_token
SIGNALWIRE_SPACE_URL=your-space.signalwire.com
SIGNALWIRE_PHONE_NUMBER=+1234567890

OPENAI_API_KEY=sk-...
ELEVENLABS_API_KEY=...
GOOGLE_API_CREDENTIALS_PATH=secrets/google.json
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

### 5. Start ngrok (for webhook testing)

```bash
ngrok http 8000
```

Copy the `https://xxxx.ngrok.io` URL and use it as your webhook base in SignalWire:

```
https://xxxx.ngrok.io/calls/signalwire/incoming
```

---

## 📞 Example Call Flow

1. Caller dials a SignalWire number
2. SignalWire webhook hits `/calls/signalwire/incoming` via ngrok
3. Audio is transcribed via Whisper (`whisper_service.py`)
4. GPT-4 generates a response (`gpt_service.py`)
5. ElevenLabs converts response to speech (`tts_service.py`)
6. AI Engine handles the full flow (`ai_engine.py`)
7. SignalWire streams the voice response back to the caller

---

## 🧹 Stack

| Purpose      | Tech Used                 |
| ------------ | ------------------------- |
| Backend API  | FastAPI (Python)          |
| Telephony    | SignalWire                |
| AI Reasoning | GPT-4 / Claude            |
| STT          | OpenAI Whisper            |
| TTS          | ElevenLabs                |
| Scheduling   | Google Calendar, Calendly |
| Deployment   | Railway, Render, Docker   |
| Dev Tunnel   | ngrok                     |

---

## 📌 Roadmap

- [x] SignalWire integration with full webhook call flow
- [x] AI response pipeline (Whisper → GPT → ElevenLabs)

### ✅ Completed

- [x] SignalWire integration with full webhook call flow
- [x] AI response pipeline (Whisper → GPT → ElevenLabs)

### 🔧 In Progress / To-Do

- [ ] Google Calendar sync
- [ ] Internal admin/test dashboard
- [ ] Multi-agent context/memory support
- [ ] Whisper integration for live STT from calls
- [ ] ElevenLabs integration with `<Play>` instead of `<Say>`
- [ ] Call transcript logging (to file/DB)
- [ ] Frontend dashboard for reviewing interactions

---

## ⚠️ Known Issues & Temporary Fixes

- **ElevenLabs Timeout / Cutoff**:

  - Long GPT responses (>20s of audio) cause timeouts or truncated playback
  - ✅ **Temporary fix**: Truncate GPT response to 200–300 characters
  - ✅ **Updated prompt**: Ask GPT to keep responses under 2 sentences
  - ✅ Added timeout handling and logging in ElevenLabs integration

- **Real-time questions** (e.g. "What time is it?") returned generic replies
  - ✅ Fix: Inject current time into GPT system prompt to simulate awareness

---

## 🛡️ License

MIT License — free to use, modify, and distribute.

---

## 👋 Contributing

PRs welcome! Let's build voice AI that actually works in the real world.

---

## 💬 Questions?

Drop an issue or ping me [@yourusername](https://github.com/yourusername).
