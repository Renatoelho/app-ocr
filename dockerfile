FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

RUN apt update && \
  apt install python3.8 \
  tesseract-ocr-all \
  python3.8-venv \
  systemctl \
  curl \
  nano \
  zip \
  unzip \
  tzdata \
  sudo -y 

RUN useradd -ms /bin/bash ocr -G sudo && \
  passwd -d ocr && \
  mkdir -p /home/ocr/python/ocr/

WORKDIR /home/ocr/python/ocr

COPY app/ .

ADD deploy/ocr.service /etc/systemd/system/

RUN su - ocr && \
  cd /home/ocr/python/ocr/ && \
  python3 -m venv .venv && \
  source .venv/bin/activate && \
  pip install -U pip setuptools wheel&& \
  pip install -r requirements.txt && \
  chown -R ocr:ocr /home/ocr

RUN systemctl daemon-reload && \
  systemctl enable ocr.service 

USER ocr

ENTRYPOINT systemctl start ocr.service 
