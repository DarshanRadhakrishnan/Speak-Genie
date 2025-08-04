# Genie Roleplay AI

A voice-interactive AI chatbot for kids that enables fun and safe roleplay conversations using speech recognition, GPT responses, and text-to-speech.

## Folder Structure

```
genie-roleplay-ai/
│
├── llm_int.py
├── voice_converter.py
├── text_converter.py
├── main.py
└── README.md
```

## Requirements

- Python 3.8+
- Node.js (for frontend)
- `ffmpeg` installed
- Whisper
- ElevenLabs API Key
- OpenAI API Key

## Setup

### Backend

```bash
pip install -r requirements.txt
export ELEVEN_LABS_API="your-elevenlabs-api-key"
export OPENAI_API_KEY="your-openai-api-key"
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Files

### `llm_int.py`

Generates GPT-based roleplay response:
```python
generate_roleplay_response(user_input, chat_history, scenario)
```

### `text_converter.py`

Records voice and transcribes using Whisper:
```python
transcribe_from_mic()
```

### `voice_converter.py`

Converts text to speech using ElevenLabs:
```python
speak(text, language="en", age_group="child")
```

## Run Flow

1. Start backend: `main.py`
2. Start frontend
3. Speak via mic
4. Whisper → GPT → ElevenLabs
5. Response plays and appears on screen

## Supported Languages

- en
- hi
- es
- fr
- de
- ta

## Supported Age Groups


- child
- teen
- adult
