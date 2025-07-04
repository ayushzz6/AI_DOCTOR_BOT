'''import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Hassan!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

#Step2: Use Model for Text output to Voice

import subprocess
import platform

from elevenlabs import save
from elevenlabs.client import ElevenLabs

from pydub import AudioSegment
import os

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is  autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")





def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "TxGEqnHWrfWFTfGW9XjX",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")'''

import os
import platform
import subprocess
from pydub import AudioSegment
from elevenlabs.client import ElevenLabs
from elevenlabs import save

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")








def text_to_speech_with_elevenlabs(input_text, output_filepath="final.mp3"):
    # Initialize ElevenLabs client
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    voice_id = "TxGEqnHWrfWFTfGW9XjX"
    model_id = "eleven_turbo_v2"
    output_format = "mp3_22050_32"

    # Get audio stream and save
    audio_stream = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice_id,
        model_id=model_id,
        output_format=output_format
    )
    save(audio_stream, output_filepath)

    # OS detection
    os_name = platform.system()

    try:
        if os_name == "Windows":
            # Convert MP3 to WAV
            wav_path = output_filepath.replace(".mp3", ".wav")
            sound = AudioSegment.from_mp3(output_filepath)
            sound.export(wav_path, format="wav")

            # Play WAV file using SoundPlayer
            subprocess.run([
                'powershell',
                '-c',
                f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'
            ])
        elif os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])  # Or use 'ffplay' or 'mpg123'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"[no] Audio playback failed: {e}")


