import os
import subprocess
import platform
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv

try:
    from elevenlabs.client import ElevenLabs
except ImportError:
    ElevenLabs = None  # If ElevenLabs is not installed

# Load environment variables from .env
load_dotenv()
ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

#Plays any audio file on any OS using playsound
def play_audio(filepath):
    try:
        playsound(filepath)
    except Exception as e:
        print(f"[no] Audio playback failed: {e}")

def text_to_speech_with_gtts(input_text, output_filepath="gtts_output.mp3"):
    try:
        print("[yes] Generating audio using gTTS...")
        audioobj = gTTS(text=input_text, lang="en", slow=False)
        audioobj.save(output_filepath)
        play_audio(output_filepath)
    except Exception as e:
        print(f"[no] gTTS failed: {e}")

def text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_output.mp3"):
    if not ElevenLabs:
        print("[no] ElevenLabs module not found. Please install it.")
        return

    if not ELEVENLABS_API_KEY:
        print("[⚠️] ELEVEN_API_KEY not set. Falling back to gTTS.")
        text_to_speech_with_gtts(input_text, output_filepath)
        return

    try:
        print("[yes] Generating audio using ElevenLabs...")
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel 
        model_id = "eleven_turbo_v2"
        output_format = "mp3_22050_32"

        audio_stream = client.text_to_speech.convert(
            text=input_text,
            voice_id=voice_id,
            model_id=model_id,
            output_format=output_format
        )

        with open(output_filepath, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

        play_audio(output_filepath)

    except Exception as e:
        print(f"[no] ElevenLabs failed: {e}")
        print(" Falling back to gTTS...")
        text_to_speech_with_gtts(input_text, output_filepath)


input_text = "hi , my name is ayush paul , i am a student of iit madras , a prominent institute of india and one of the top colleges in india."
text_to_speech_with_gtts(input_text, output_filepath="output_autoplay.mp3")