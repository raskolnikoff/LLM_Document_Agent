LLM Document Agent (Docker Edition)
===================================

Overview
--------
A local, containerized LLM document Q&A agent powered by Ollama and Gradio.
With the latest update, the system delivers highly accurate, context-rich answers from your documents, with lightning-fast and privacy-first local inference.
The enhanced prompt engineering and RAG architecture now provide detailed, human-like explanations for any supported content.

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
    │   └── gradio_ui.py
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

2. Build and Launch with Docker Compose
`````````
docker compose up --build
# or
docker-compose up --build
`````````

Starts both the 'ollama' LLM backend and the 'llm_gradio' web frontend.

3. (Once) Download Your Model in the Ollama Container

````````
docker ps
docker exec -it ollama bash
ollama pull llama3
# Replace "llama3" with any available model if desired
````````
4. Restart Gradio UI (if you pulled after first launch)

````````
docker compose restart llm_gradio
````````

5. Open the Web UI

Visit: http://localhost:7860

Key Features
------------
- Detailed, context-rich answers thanks to advanced prompt engineering and RAG integration
- Fully local and private: No data leaves your machine—runs entirely via Docker & Ollama
- Reproducible deployment: Any machine with Docker can instantly host the same environment
- Lightning fast: Llama3 provides state-of-the-art accuracy and speed for most use-cases
- Easy extensibility: Future backends (HuggingFace, LMStudio, vLLM) are planned

Known Issues / Troubleshooting
------------------------------
- Model not found: Run 'ollama pull llama3' inside the container before querying
- Startup/Timeout: Wait for Ollama to fully load the model, or check RAM (16GB+ recommended)
- CPU inference is slow: For best speed, use GPU if/when supported by Docker Ollama
- Automatic Model Pull: Manual model download is required after container starts (automation in roadmap)

Roadmap
-------
- [ ] Automate model download during startup
- [ ] Health check and readiness probe scripts
- [ ] Support additional LLM backends
- [ ] GPU support (as soon as available in Ollama Docker)
- [ ] Enhanced admin/monitoring tools

Contributing
------------
Pull Requests and Issues are welcome!
For questions or support, please open an issue on GitHub.

(c) 2025 AiDevOps Project / [Tokyoyabanjin]