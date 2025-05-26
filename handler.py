import runpod

def handler(event):
    return {"output": "OK"}

runpod.serverless.start({"handler": handler})
