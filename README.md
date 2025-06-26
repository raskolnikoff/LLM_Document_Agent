LLM Document Agent (Docker Edition)
===================================

Overview
--------
A local, containerized LLM document Q&A agent powered by Ollama and Streamlit.
This production-ready Docker deployment delivers highly accurate, context-rich answers from your documents with lightning-fast, privacy-first local inference.
The enhanced prompt engineering and RAG architecture provide detailed, human-like explanations for any supported content.

Docker support enables reproducible, zero-config deployment on any environment.

Prerequisites
-------------
- Docker Desktop (macOS/Windows/Linux)
- Docker Compose v2
- At least 16GB RAM recommended (minimum 8GB for small models)
- (Optional, for dev) git, curl, bash

Project Structure
-----------------
    .
    ├── app/
    │   └── web_ui.py
    ├── docker-compose.yml
    ├── Dockerfile
    ├── requirements.txt
    ├── README-dockerize.md
    └── (other supporting files/folders)

Quick Start
-----------
1. Clone the Repository

````````
git clone https://github.com/<your-repo>/LLM_Document_Agent.git
cd LLM_Document_Agent
````````

2. Build and Launch with Docker Compose (includes automatic Ollama model pull)

`````````
docker compose up --build
# or
docker-compose up --build
`````````

This starts both the 'ollama' LLM backend and the 'llm_streamlit' web frontend. The Ollama container automatically pulls the configured model during startup, so no manual intervention is needed.

3. Open the Web UI

Visit: http://localhost:8501

Advanced: Manual Model Pull (Optional)
--------------------------------------
If you prefer to manually pull or change models, you can enter the Ollama container and pull models yourself:

````````
docker ps
docker exec -it ollama bash
ollama pull llama3
# Replace "llama3" with any available model if desired
````````

After manual model pull, restart the Streamlit UI to apply changes:

````````
docker compose restart llm_streamlit
````````

Key Features
------------
- Detailed, context-rich answers thanks to advanced prompt engineering and RAG integration
- Fully local and private: No data leaves your machine—runs entirely via Docker & Ollama
- Production-ready, reproducible deployment: Any machine with Docker can instantly host the same environment
- Lightning fast: Llama3 provides state-of-the-art accuracy and speed for most use-cases
- Easy extensibility: Future backends (HuggingFace, LMStudio, vLLM) are planned

Known Issues / Troubleshooting
------------------------------
- Startup/Timeout: Wait for Ollama to fully load the model; 16GB+ RAM recommended for best performance
- CPU inference is slow: For best speed, use GPU if/when supported by Docker Ollama
- Model not found: The container now automatically pulls the configured model at startup. If issues persist, check logs for errors.

Roadmap
-------
- [x] Automate model download during startup (implemented via entrypoint script)
- [ ] Health check and readiness probe scripts
- [ ] Support additional LLM backends
- [ ] GPU support (as soon as available in Ollama Docker)
- [ ] Enhanced admin/monitoring tools

Entrypoint Script (/bin/init-entrypoint.sh)
-------------------------------------------
This script runs automatically when the Ollama container starts. It checks for the presence of the configured LLM model and pulls it if not already available. This ensures the model is ready before the service starts, enabling seamless and automated deployment without manual steps.

Contributing
------------
Pull Requests and Issues are welcome!
For questions or support, please open an issue on GitHub.

(c) 2025 AiDevOps Project / [Tokyoyabanjin]