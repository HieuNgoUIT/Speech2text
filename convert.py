from os import path
from pydub import AudioSegment

# files                                                                         
src = "3.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound = sound.set_channels(1)
sound.export(dst, format="wav")

# from pydub import AudioSegment
# sound = AudioSegment.from_wav("/path/to/file.wav")
# sound = sound.set_channels(1)
# sound.export("/output/path.wav", format="wav")