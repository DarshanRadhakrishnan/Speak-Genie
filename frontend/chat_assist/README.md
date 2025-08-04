
# 🧠 SpeakGenie Frontend (React)

This is the React frontend for SpeakGenie, an interactive AI-based voice assistant platform designed for children. It allows users to either speak with an AI tutor or participate in roleplay scenarios for conversational learning.

---

## 📁 Project Structure

```
src/
├── App.jsx                # Routing entry point
├── HomePage.jsx          # Home UI with avatar, language selection, and mode options
├── chat_Assist1.jsx      # AI Tutor chat page
├── chat_Assist2.jsx      # Roleplay chat page
├── assets/
│   ├── pet-avatar.gif    # Avatar animation
│   └── click-sound.mp3   # Button click sound
├── HomePage.css          # Styles for HomePage
├── chatAssist1.css       # Styles for Tutor Chat
└── chatAssist2.css       # Styles for Roleplay Chat
```

---

## 🚀 How to Run

1. Ensure the Python backend (port **8000**) and Express server (port **5000**) are running.
2. Start the frontend:

```bash
npm install
npm run dev  # or npm start depending on setup
```

Frontend usually runs on: [http://localhost:5173](http://localhost:5173)

---

## 🔄 API Communication

| Component         | API Endpoint                         | Method | Description |
|------------------|--------------------------------------|--------|-------------|
| ChatTutor        | http://localhost:5000/api/ask        | POST   | Gets user question + AI tutor response |
| ChatRoleplay     | http://localhost:5000/api/roleplay   | POST   | Gets user question + AI roleplay response |
| Express Backend  | http://localhost:5000                | -      | Proxy to Python backend |
| Python Backend   | http://localhost:8000/ask            | POST   | Core AI logic (text/audio based) |

---

## 📜 Components Summary

### 1. `HomePage.jsx`
- Welcome interface.
- Shows avatar, user progress, language selector.
- Navigation buttons to tutor or roleplay chat.
- Sound effect on button click.

### 2. `chat_Assist1.jsx` (Tutor Mode)
- Simple chat box.
- Sends audio/text and receives an educational response.
- Stores conversation history in `useState`.
- Mic button for interaction.

### 3. `chat_Assist2.jsx` (Roleplay Mode)
- Includes inputs for `language`, `ageGroup`, and `scenario`.
- Chat history with alternating roles (`user` and `assistant`).
- Mic button to start interaction.

### 4. `App.jsx`
- Handles routing between homepage, tutor, and roleplay components using React Router.

---

## 🔧 Dependencies

Install required packages:

```bash
npm install axios react-router-dom
```

---

## 🌐 Ports Used

| Service            | Port  |
|--------------------|-------|
| Python Backend     | 8000  |
| Express Middleware | 5000  |
| React Frontend     | 5173  (default with Vite) |

---

## 📌 Routes

| Path             | Description |
|------------------|-------------|
| `/`              | Home page   |
| `/chat-tutor`    | Tutor Mode  |
| `/chat-roleplay` | Roleplay Mode |

---

## 👶 Example Use Flow

1. User opens [http://localhost:5173](http://localhost:5173)
2. Chooses a language and clicks a chat mode.
3. Speaks through the mic.
4. Frontend sends data to Express → Python → GPT.
5. GPT responds and the frontend updates the chat.

---

Enjoy building with SpeakGenie! 🧚‍♂️✨
