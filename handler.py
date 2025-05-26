import runpod
from inference import run_musetalk

def handler(event):
    input_data = event["input"]
    audio_b64 = input_data.get("audio")
    video_b64 = input_data.get("video")
    result = run_musetalk(audio_b64, video_b64)
    return {"output": result}

runpod.serverless.start({"handler": handler})
