FROM ubuntu:20.04

RUN apt-get update -y && apt-get install -y \
    libsdl2-dev \
    python3.9 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install -U pyxel
WORKDIR /var
COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

WORKDIR  /var

# COPY script.py .
ENTRYPOINT ["pyxel", "copy_examples"]
