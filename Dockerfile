# Dockerfile for LLM_Document_Agent - Gradio/Streamlit version
# Maintainer: Max

FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl git && apt-get clean

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install gradio

COPY . .

EXPOSE 8501

CMD streamlit run app/web_ui.py --server.port=8501 --server.address=0.0.0.0