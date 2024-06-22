from pydub import AudioSegment
from pydub.playback import play

import speech_recognition as sr #this one not work now still firgure it out
from pydub import AudioSegment

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
audio_file = "path/to/your/audiofile.mp3"  # Update this to your audio file path
text_file = "path/to/your/outputfile.txt"  # Update this to your desired output text file path
audio_to_text(audio_file, text_file)

