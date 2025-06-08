#!/bin/bash

set -e

# Pipeline for RAG setup and execution

# 1. Parse documents
PYTHONPATH=. python ingest/parser.py

# 2. Chunk and embed
PYTHONPATH=. python ingest/chunk_embed.py

# 3. UI launch logic
if [ "$1" == "--cli" ]; then
  PYTHONPATH=. python app/ui.py
# run_pipeline.sh
elif [ "$1" == "--gui" ]; then
  PYTHONPATH=. streamlit run app/web_ui.py
else
  echo "Usage: ./run_pipeline.sh [--cli | --gui]"
  exit 1
fi
