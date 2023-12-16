import os
import whisper
from pydub.utils import make_chunks
from pydub import AudioSegment
from whisper.utils import get_writer

def get_choice(prompt, choices):
    choices_string = ""
    for idx, filename in enumerate(choices):
        choices_string += f"{idx}: {filename}\n"
        
    choice = input(f"{prompt}\n{choices_string}")
    while True:
        try:
            choice_number = int(choice.strip())
            if choice_number < 0 or choice_number >= len(choices):
                raise ValueError
        except ValueError:
            choice = input(f"oops try again: \n{choices_string}")
            continue
        break
    return choice_number
        
OUTPUT_DIR = "output_files"
INPUT_DIR = "input_files"
AUDIO_FILE_EXTENSIONS = (
    '.avi',
    '.oma',
    '.wav',
    '.mid',
    '.flac',
    '.cda',
    '.db',
    '.mp4',
    '.m3u',
    '.mp3',
    '.MP3',
    '.m4a',
    '.mkv',
    '.wav',
    '.mP3',
)

TRANSCRIPTION_OPTIONS = [
    "Whole file at once",
    "Whole file in 1 minute chunks",
    "Whole file in 5 minute chunks",
    "Specific time frame",
] 

audio_files = [
    filename for filename in os.listdir("input_files/") 
    if filename.endswith(AUDIO_FILE_EXTENSIONS)
]


target_file = audio_files[
    get_choice("Choose a file to transcribe:", audio_files)
]
print(target_file + "\n")

method = TRANSCRIPTION_OPTIONS[
    get_choice("Choose a transcription method:", TRANSCRIPTION_OPTIONS)
]
print(method + "\n")

if method == "Whole file at once":
    print("Transcribing whole file at once")
    model = whisper.load_model("base")
    result = model.transcribe(os.path.join(INPUT_DIR, target_file))
    writer = get_writer("srt", OUTPUT_DIR)
    audio_path = os.path.join(OUTPUT_DIR, f"TRANSCRIPTION_WHOLE_FILE_{target_file}.srt")
    writer(result, audio_path, **{
        'highlight_words': False, 'max_line_count': None, 'max_line_width': None, 'max_words_per_line': None
    })

elif method == "Whole file in 1 minute chunks":
    print("Transcribing whole file in 1 minute chunks")
    model = whisper.load_model("base")
    chunks = make_chunks(
        AudioSegment.from_mp3(
            os.path.join(INPUT_DIR, target_file)
        ),
        60000
    )
    for c in chunks:
        chunk_path = os.path.join(
            OUTPUT_DIR, f"1_MINUTE_CHUNK_{chunks.index(c)}_{target_file}.mp3"
        )
        c.export(chunk_path, format="mp3")

        result = model.transcribe(chunk_path)
        writer = get_writer("srt", OUTPUT_DIR)
        audio_path = os.path.join(OUTPUT_DIR, f"1_MINUTE_TRANSCRIPT_{chunks.index(c)}_{target_file}.srt")
        writer(result, audio_path, **{
            'highlight_words': False, 'max_line_count': None, 'max_line_width': None, 'max_words_per_line': None
        })



elif method == "Whole file in 5 minute chunks":
    print("Transcribing whole file in 5 minute chunks - TODO")
elif method == "Specific time frame":
    print("Transcribing specific time frame - TODO")
else:
    print("Something went wrong, bye!")


# choices = ""
# for idx, filename in enumerate(audio_files):
#     choices += f"{idx}: {filename}\n"

# file_choice = None
# while file_choice is None:

# file_choice = input("Choose a file to transcribe:\n" + choices)
 
