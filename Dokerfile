FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=on \
    SHELL=/bin/bash

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# System dependencies
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
      python3-dev \
      python3-pip \
      python3.10-venv \
      git \
      git-lfs \
      wget \
      curl \
      ffmpeg \
      unzip \
      libsm6 \
      libxext6 \
      libgl1 \
      libglib2.0-0 \
      libgoogle-perftools-dev \
      procps && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean -y

# Set working directory
WORKDIR /workspace

# Clone MuseTalk
RUN git clone https://github.com/ChiWeiHsiao/MuseTalk.git
WORKDIR /workspace/MuseTalk

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    pip3 install onnxruntime-gpu moviepy runpod

# Download model checkpoint
RUN mkdir -p checkpoints && \
    wget -O checkpoints/musetalk.pth https://huggingface.co/ChiWeiHsiao/MuseTalk/resolve/main/musetalk.pth

# Copy serverless handler and support files
COPY --chmod=755 handler.py /workspace/MuseTalk/handler.py
COPY --chmod=755 inference.py /workspace/MuseTalk/inference.py
COPY --chmod=755 start.sh /start.sh

# Entry point
ENTRYPOINT /start.sh
