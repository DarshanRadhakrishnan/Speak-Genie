from pydantic import BaseModel
from fastapi import FastAPI,Form
from text_converter import transcribe_from_mic
from RAG import final_rag_chain
from voice_converter import speak
import os
api=FastAPI()

class queryRequest(BaseModel):# we are creating a class for the input parameter beacuse when an api request is made from the router with a single dictionary of params and that is considered as the object here
    language: str = "en"
    age_group: str = "child"

@api.post('/ask')#this is how we need to make a ap post req handler with fastapi
def run_voice_assistant(req:queryRequest):
    question = transcribe_from_mic()
    answer = final_rag_chain(question)
    audio_path=speak(answer, language=req.language, age_group=req.age_group)
    return {
        "question":question,
        "answer":answer,
        "audio_url": f"/audio/{os.path.basename(audio_path)}"# here anyway since we have used olay in the speak() function the sound will be played already but we can also send the voice file path to the front end which can play whenever needed using <audio>
    }
