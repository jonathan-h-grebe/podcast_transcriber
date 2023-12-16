from pydub import AudioSegment

FILE_NAME="ADHD-DIAGNOSIS-FULL-EP-v3-encoded.wav"

song = AudioSegment.from_wav(FILE_NAME)
# AudioSegment.from_wav
ten_seconds = 10 * 1000
sixty_seconds = 60 * 1000

# first_10_seconds = song[:ten_seconds]
first_60_seconds = song[:sixty_seconds]

first_60_seconds.export("ADHD-DIAGNOSIS-FULL-EP-v3-encoded-60s.mp3", format="mp3")
