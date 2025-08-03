from elevenlabs import generate, play, save, set_api_key, voices
import tempfile
import os

set_api_key(os.environ("ELEVEN_LABS_API"))

#next we need to create function that gives the voice id depending on the age and language from the availbale voice
def get_voice_id(language="en", age_group="child"):
    voice_presets = {
        "en": {
            "child": "Rachel",      # Soft, cheerful (child-friendly)
            "teen": "Bella",        # Friendly, expressive
            "adult": "Matthew",     # Neutral, clear
        },
        "hi": {
            "child": "Rishi",       # Hindi male, gentle
            "teen": "Anaya",        # Hindi female, warm
            "adult": "Prem",        # Hindi male, deep
        },
        "es": {  # Spanish
            "child": "Sofia",
            "teen": "Mateo",
            "adult": "Carlos",
        },
        "fr": {  # French
            "child": "Chloe",
            "teen": "Lucas",
            "adult": "Antoine",
        },
        "de": {  # German
            "child": "Lena",
            "teen": "Finn",
            "adult": "Jonas",
        },
        "ta": {  # Tamil
            "child": "Kaviya",
            "teen": "Pranav",
            "adult": "Sundar",
        }
    }

    lang = language.lower()[:2]
    voice_name = voice_presets.get(lang, voice_presets["en"]).get(age_group, "Rachel")#so here depending on the input parameters (age and lang) we
     #will decode what is the name of the that type and with that we can sea4rch it in the stored voices in the eleven labs
    for v in voices():
        if v.name == voice_name:
            return v.voice_id
    raise ValueError(f"Voice '{voice_name}' not found.")

#once after geetinng the voice_id based upon our need we can generate the audio

# 🔊 Generate and play speech
def speak(text, language="en", age_group="child", play_audio=True):# by default we will have the language as englisha and the age as child
    voice_id = get_voice_id(language, age_group)
    audio = generate(
        text=text,
        voice=voice_id,
        model="eleven_monolingual_v1" if language.startswith("en") else "eleven_multilingual_v1"
    )

    if play_audio:
        play(audio)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        save(audio, f.name)
        print(f"✅ Audio saved to: {f.name}")
        return f.name # we return the name of the file as output
