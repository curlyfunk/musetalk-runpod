import base64
import tempfile
import os
from io import BytesIO
from moviepy.editor import VideoFileClip
from inference import inference_pipeline  # това идва от MuseTalk

def save_base64_to_file(b64_data, suffix):
    decoded = base64.b64decode(b64_data)
    fd, path = tempfile.mkstemp(suffix=suffix)
    with os.fdopen(fd, 'wb') as f:
        f.write(decoded)
    return path

def file_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def run_musetalk(audio_b64, video_b64):
    audio_path = save_base64_to_file(audio_b64, ".wav")
    video_path = save_base64_to_file(video_b64, ".mp4")
    output_path = "output/output.mp4"

    # Тук се изпълнява MuseTalk inference
    inference_pipeline(audio_path=audio_path, video_path=video_path, output_path=output_path)

    return file_to_base64(output_path)
