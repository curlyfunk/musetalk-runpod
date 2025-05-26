FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y ffmpeg curl git && \
    rm -rf /var/lib/apt/lists/*

COPY handler.py .
COPY start.sh /start.sh

RUN pip install --no-cache-dir runpod

ENTRYPOINT ["/start.sh"]
