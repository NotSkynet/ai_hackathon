import os
from pydub import AudioSegment
import speech_recognition as sr

# Set the path to the local ffmpeg and ffplay executables
ffmpeg_path = os.path.join(os.path.dirname(__file__), 'bin')
os.environ["PATH"] += os.pathsep + ffmpeg_path

def audio_to_text(audio_file, text_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Convert audio to WAV format if necessary
    if not audio_file.endswith('.wav'):
        sound = AudioSegment.from_file(audio_file)
        audio_file = "converted.wav"
        sound.export(audio_file, format="wav")

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # read the entire audio file

    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription: " + text)
    except sr.UnknownValueError:
        text = "Speech recognition could not understand audio"
    except sr.RequestError as e:
        text = f"Could not request results from Google Web Speech API; {e}"

    # Save the transcription to a text file
    with open(text_file, "w") as file:
        file.write(text)

# Example usage
current_dir = os.path.dirname(__file__)
audio_file = os.path.join(current_dir, 'Audio', 'recording.wav')
text_file = os.path.join(current_dir, 'outputfile.txt')
audio_to_text(audio_file, text_file)
