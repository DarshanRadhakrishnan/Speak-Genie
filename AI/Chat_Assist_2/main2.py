import fastapi
from text_converter_2 import transcribe_from_mic
from llm_int import generate_roleplay_response
from voice_converter_2 import speak
from pydantic import BaseModel
import os
api=fastapi()

class queryRequest(BaseModel):# we are creating a class for the input parameter beacuse when an api request is made from the router with a single dictionary of params and that is considered as the object here
    language: str = "en"
    age_group: str = "child"
    chat_history:list ="[{}]"
    scenario: str= "At the Store"
@api.post('/ask')#this is how we need to make a ap post req handler with fastapi
def run_voice_assistant(req:queryRequest):
    question = transcribe_from_mic()
    answer=generate_roleplay_response(question,req.chat_history,req.scenario)
    audio_path=speak(answer,req.language,req.age_group)
    return {
        "question":question,
        "answer":answer,
        "audio_url": f"/audio/{os.path.basename(audio_path)}"
    }
