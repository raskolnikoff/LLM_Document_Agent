import os
import requests
import gradio as gr
import json

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "ollama")
OLLAMA_PORT = 11434
OLLAMA_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3")


def document_agent_qa(query):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": query,
        # "stream": False   ← Remove, as API always streams!
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120)
        answer = ""
        for line in resp.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                answer += chunk.get("response", "")
                if chunk.get("done"):
                    break
        if not answer:
            answer = "(No answer returned from LLM.)"
        return answer
    except Exception as e:
        return f"Error: {e}"


with gr.Blocks() as demo:
    gr.Markdown("# LLM Document Agent Demo (Gradio Edition)")
    gr.Markdown(
        """
        ⚠️ Ollama server must be running locally or in a Docker container (see README).

        - This demo runs reliably on Docker/Cloud, unlike Streamlit+Torch.
        - For full functionality, ensure your backend/service URLs are set in the environment/config.
        """
    )

    inp = gr.Textbox(label="Ask a question about your documents:")
    out = gr.Textbox(label="Answer:")
    btn = gr.Button("Submit")
    btn.click(document_agent_qa, inp, out)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
