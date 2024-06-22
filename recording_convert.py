from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("Audio/recording.wav", format="wav")
play(sound)