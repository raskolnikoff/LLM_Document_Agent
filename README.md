
# LLM Document Agent (Docker Edition)

## Overview

This project enables a **local, containerized LLM document Q&A agent** powered by [Ollama](https://ollama.com/) and [Gradio](https://gradio.app/).  
The Docker setup provides a reproducible, easily deployable environment for running LLM-based Q&A via web UI.

---

## Prerequisites

- Docker Desktop (macOS/Windows/Linux)  
- Docker Compose v2  
- At least **16GB RAM** recommended for smooth LLM inference (minimum 8GB for small models)
- (Optional, for dev) git, curl, bash

---

## Project Structure

```
.
├── app/
│   └── gradio_ui.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README-dockerize.md   # ← This file!
└── (other supporting files/folders)
```

---

## Quick Start: Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-repo>/LLM_Document_Agent.git
cd LLM_Document_Agent
```

### 2. Build and Launch the Containers

```bash
docker compose up --build
# or
docker-compose up --build
```

> This will start the following containers:
> - `ollama` (LLM backend)
> - `llm_gradio` (Gradio web UI frontend)

### 3. Enter the Ollama Container to Download Your Model

Ollama **does NOT pull models automatically in Docker**.
You must manually pull a model after the container starts.

```bash
# List running containers to get ollama CONTAINER ID or use the service name 'ollama'
docker ps
docker exec -it ollama bash
# Inside the ollama container, run:
ollama pull llama3
# You can replace "llama3" with any other available model
```

### 4. (Re)Start the Gradio UI Container  
(If you pulled the model after first launch, you may need to restart the UI for connectivity.)

```bash
docker compose restart llm_gradio
```

### 5. Access the Web UI

Visit:  
[http://localhost:7860](http://localhost:7860)  
You should see the Gradio UI and be able to interact with the LLM!

---

## Known Issues / Troubleshooting

- **HTTPConnectionPool/Timeout**  
  If you see errors like `Read timed out` or HTTP 500, it's usually because:
  - The model isn't pulled yet
  - Ollama is still loading the model (wait, watch docker logs)
  - Not enough memory: Increase Docker's RAM allocation to **16GB** or more

- **Model Not Found**
  - Run `ollama pull <model>` in the container before starting queries

- **Performance**  
  - LLM inference on CPU is slow; for large models, prefer GPU machines (TBA for official Docker GPU support)
  - For heavy traffic or production, consider a separate inference backend and autoscaling.

- **Automatic Model Pull**  
  - As of now, you *must* manually enter the ollama container to pull your desired model.

---

## Roadmap & Anticipated Challenges

### Short Term

- [ ] **Automate ollama pull** in the Docker build/startup process
    - Workaround: Provide an entrypoint or `command` in docker-compose, or use `init` scripts
    - Issue: Ollama model pulls are large and can cause container timeouts or image bloat if done at build-time

- [ ] **Streamlined Health Checks**  
    - Add scripts to verify that both Ollama and Gradio are healthy and ready before accepting queries

- [ ] **Parameterize Model via ENV**  
    - Enable model selection via docker-compose `.env` file

### Mid to Long Term

- [ ] **Production-Ready Deployment**  
    - Secure endpoints
    - Reverse proxy support (nginx/caddy)
    - GPU inference support (when supported by ollama in Docker)

- [ ] **Documentation Improvements**  
    - Step-by-step videos
    - Advanced configuration tips (memory tuning, concurrency, etc.)

- [ ] **Multi-backend Flexibility**  
    - Support other LLM backends (LMStudio, vLLM, HuggingFace Text Generation Inference) as drop-in options

- [ ] **User Feedback and Monitoring**  
    - Add logging, stats dashboard

---

## Contact & Contributions

Pull Requests and Issues are welcome!  
For questions or support, please open an issue on GitHub.

---

**(c) 2025 AiDevOps Project / [your team/org]**
