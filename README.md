# Speak-Genie

SpeakGenie is a real-time AI voice tutor for kids (6–16) to practice English in a fun and interactive way.

## 🌟 Features

- 🎤 **Free Talk Mode**: Kids can speak freely with the AI using their microphone.
- 🎭 **Roleplay Mode**: Practice real-life English with scenarios like “🏫 At School” or “🛒 At the Store”.
- 🧠 Powered by **Whisper** (STT), **OpenAI GPT** (LLM), and **TTS** (like ElevenLabs) for full voice interaction.
- 🗣️ Supports native language playback based on selected language input.
- 🧒 Designed for simplicity and fun with emoji feedback and gamified experience (e.g., streaks, levels).
- 🌐 **Languages**: English 🇺🇸, Hindi 🇮🇳, Spanish 🇪🇸 (expandable)

---

## 🚀 Project Structure

### 🧩 Frontend (React)
| File | Description |
|------|-------------|
| `HomePage.jsx` | Welcome screen with language selector and navigation to modes |
| `chat_Assist1.jsx` | "Speak with Tutor" mode (Free conversation) |
| `chat_Assist2.jsx` | "Roleplay" mode with scenario and character setup |
| `App.jsx` | Handles routing between components |
| `chatAssist1.css`, `chatAssist2.css`, `HomePage.css` | Styling for respective components |

### 🧠 Backend APIs Required

To make the frontend fully functional, the following backend APIs **must be running**:

#### 🔹 FastAPI (Python backend)

| Endpoint | Description |
|----------|-------------|
| `POST http://localhost:8000/ask` | Processes STT input and responds with a GPT-generated answer (for tutor mode) |
| `POST http://localhost:8000/ask_role` | Handles scenario-based roleplay conversations using LLM (GPT) |

> ⚠️ Port `8000` must be open and available.

#### 🔹 Express.js (Optional middleware proxy)

| Endpoint | Description |
|----------|-------------|
| `POST http://localhost:5000/api/ask` | Proxies to FastAPI `/ask` endpoint |
| `POST http://localhost:5000/api/roleplay` | Proxies to FastAPI `/ask_role` endpoint |

> ⚠️ Port `5000` must be open if using Express as intermediary.

---

## 📦 Requirements

### Frontend

- Node.js >= 18.x
- React 18+
- `axios`, `react-router-dom`

### Backend (Python FastAPI)

- Python >= 3.9
- `fastapi`, `uvicorn`, `openai`, `whisper`, `scipy`, `elevenlabs` (TTS)

---

## 🛠️ How to Run

### 🔧 Backend
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn main:app --reload --port 8000
```

### ⚙️ Express Middleware (Optional)
```bash
cd backend/
npm install
node index.js
```

### 🎨 Frontend
```bash
cd frontend/
npm install
npm start
```

Visit: [http://localhost:3000](http://localhost:3000)

---

## 📁 Notes

- Audio is captured using mic button.
- User and AI messages are styled left/right respectively.
- Language, scenario, and age group inputs are available in roleplay mode.
- Use animated avatars and sound feedback to engage users.

---

## 🔐 Environment Variables (if needed)

Create `.env` file in backend directory:
```env
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

---


Made with ❤️ for young learners.

