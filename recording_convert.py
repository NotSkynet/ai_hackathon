import os
import openai
from pydub import AudioSegment

# Set the path to the local ffmpeg and ffplay executables
ffmpeg_path = os.path.join(os.path.dirname(__file__), 'bin')
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Initialize OpenAI client using the API key from the environment variable
api_key = "sk-proj-Z3QTkb8pzow4wQTFb0FtT3BlbkFJbjs3JSqSocrBf0vsEaom"
client = openai.OpenAI(api_key=api_key)

def split_audio(audio_file, chunk_size_ms=60000):  # 1 minute = 60000 ms
    """Split audio file into smaller chunks."""
    audio = AudioSegment.from_file(audio_file)
    chunks = []
    for i in range(0, len(audio), chunk_size_ms):
        chunk = audio[i:i + chunk_size_ms]
        chunks.append(chunk)
    return chunks

def transcribe_audio_chunk(chunk, chunk_index):
    """Transcribe a chunk of audio."""
    temp_audio_file = f"chunk_{chunk_index}.wav"
    chunk.export(temp_audio_file, format="wav")
    
    with open(temp_audio_file, "rb") as audio:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio,
            response_format="json"
        )
        os.remove(temp_audio_file)
        return response.text

def audio_to_text(audio_file, text_file):
    chunks = split_audio(audio_file)
    full_transcription = ""

    for index, chunk in enumerate(chunks):
        try:
            print(f"Transcribing chunk {index + 1}/{len(chunks)}...")
            chunk_transcription = transcribe_audio_chunk(chunk, index)
            full_transcription += chunk_transcription + "\n"
        except Exception as e:
            print(f"Error transcribing chunk {index + 1}: {e}")

    # Save the full transcription to a text file
    try:
        with open(text_file, "w") as file:
            file.write(full_transcription)
    except Exception as e:
        print(f"Error saving transcription to file: {e}")

# Example usage
current_dir = os.path.dirname(__file__)
audio_file = os.path.join(current_dir, 'Audio', 'recording.wav')
text_file = os.path.join(current_dir, 'outputfile.txt')
audio_to_text(audio_file, text_file)