# voice_to_text.py

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import time

SAMPLE_RATE = 16000
SILENCE_THRESHOLD = 0.005  # volume threshold 
SILENCE_DURATION = 3    # seconds of silence before stopping which is increased for children
CHUNK_DURATION = 0.2      # seconds per chunk

def transcribe_from_mic():
    recorded = []
    silence_start = None

    print("🎙️ Start speaking...")

    def is_silent(data): #Since the wav file is just a list of 16 bit intgers representing the amplitudes at every time second we check the mean of it and if its < threshoold it is considered as silence
        return np.abs(data).mean() < SILENCE_THRESHOLD

    try:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1) as stream: #this is sd.InputStream is the one whoch hears the audio live
            while True:
                chunk, _ = stream.read(int(SAMPLE_RATE * CHUNK_DURATION)) #this atcually reads the input voice
                recorded.append(chunk)

                if is_silent(chunk):
                    if silence_start is None:
                        silence_start = time.time()
                    elif time.time() - silence_start > SILENCE_DURATION:
                        print("⏹️ Detected silence. Stopping.")
                        break
                else:
                    silence_start = None

    except KeyboardInterrupt:
        print("❌ Recording stopped manually.")

    # Save audio
    recorded_np = np.concatenate(recorded, axis=0)
    write("recorded.wav", SAMPLE_RATE, recorded_np) #this is the place where we create a wav file 

    # Transcribe
    print("🧠 Transcribing with Whisper...")
    model = whisper.load_model("base") #then we intialise the whisper model "base" is the version and it is for typical  for medium data
    result = model.transcribe("recorded.wav") #this is the transfer into text part
    print("\n📝 Transcription:\n", result["text"])
    
    return result["text"]
