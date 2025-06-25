# Dockerfile for LLM_Document_Agent - Gradio version
# Maintainer: Max

FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl git && apt-get clean

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gradio

COPY . .

EXPOSE 7860

CMD python app/gradio_ui.py
