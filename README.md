# podcast_transcriber
Split and generate transcriptions for audio files

## Setup
Windows PC
### 1 install python on windows

### 2. install ffmpeg
via [scoop](https://scoop.sh/) or [binaries](https://ffmpeg.org/download.html#build-windows) 

### 3. start cmd line
windows key -> "cmd" -> Enter


### 4. make venv
```
py -m venv .env
```

### 5. go into venv 
```
.env\Scripts\activate
```

### 6. install dependencies 
```
pip install -r requirements.txt
```

# Usage
1. start cmd: windows key -> "cmd" -> Enter
2. put mp3 file into "input_files"
3. start env
```
.env\Scripts\activate
```
4. python podcast_transcriber.py