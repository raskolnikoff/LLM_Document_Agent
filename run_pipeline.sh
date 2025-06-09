#!/bin/bash

set -e

# Pipeline for RAG setup and execution

# Start Ollama server in background
echo "🔄 Starting Ollama..."
ollama serve > /dev/null 2>&1 &

# Step 1: Parse documents
echo "📄 Parsing documents..."
PYTHONPATH=. python ingest/parser.py

# Step 2: Chunk and embed
echo "🧠 Embedding chunks..."
PYTHONPATH=. python ingest/chunk_embed.py

# 3. UI launch logic
if [ "$1" == "--cli" ]; then
  PYTHONPATH=. python app/ui.py
elif [ "$1" == "--gui" ]; then
  PYTHONPATH=. streamlit run app/web_ui.py
else
  echo "Usage: ./run_pipeline.sh [--cli | --gui]"
  exit 1
fi
