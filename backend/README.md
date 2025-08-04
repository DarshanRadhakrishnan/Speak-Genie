# 🚀 Express Backend for AI Tutor & Roleplay Assistant

This Express-based backend connects your React frontend with a Python FastAPI service. It handles POST requests and forwards them to FastAPI endpoints for AI-based tutor and roleplay conversations.

---

## 🌐 Server Details

- **Express Backend Port:** `3001`
- **Python FastAPI Port:** `8000`
- **FastAPI URL (used internally):** `http://localhost:8000/ask`

---

## 📁 Folder Structure

```
backend/
├── router.js
├── index.js             
└── package.json
```

---

## 📦 Installation

Make sure you have **Node.js** and **npm** installed.

```bash
npm install
```

---

## ▶️ Running the Server

```bash
node app.js
```

Make sure the **FastAPI server** is already running on port **8000**.

---

## 📡 API Endpoints

### 1. `POST /api/ask`

For tutor assistant responses.

**Request Body:**
```json
{
  "language": "en",
  "ageGroup": "child"
}
```

**Forwarded to:** `http://localhost:8000/ask`

---

### 2. `POST /api/ask_role`

For roleplay scenario-based responses.

**Request Body:**
```json
{
  "language": "en",
  "ageGroup": "child",
  "chatHistory": [
    { "role": "user", "content": "Hello!" },
    { "role": "assistant", "content": "Hi there! How can I help you today?" }
  ],
  "scenario": "🎭 At the Bakery"
}
```

**Forwarded to:** `http://localhost:8000/ask`

---

## 🛠 Troubleshooting

- Make sure the FastAPI backend is running before making requests.
- If you're getting a 500 error, ensure that Python server is listening at `http://localhost:8000/ask` and can parse the request JSON properly.
- Check for port conflicts between frontend (React), backend (Express), and API (FastAPI).

---



---

Happy coding! 💻✨
