# g4f-n1 — Open-Source AI Wrapper Like g4f

A lightweight, OpenAI-compatible API wrapper that routes requests to multiple open-source or public large language model (LLM) backends — similar in spirit to [g4f](https://github.com/xtekky/g4f), but fully open and customizable.

---

## Features

- FastAPI-based REST API with `/v1/chat/completions` endpoint  
- Supports pluggable providers (e.g., Mistral 7B local model, Gemini API)  
- Standardized OpenAI API schema (messages, roles, models)  
- Easy to add new model backends or APIs  
- Modular, clean project structure

---

## Getting Started

### Requirements

- Python 3.9+  
- CUDA-enabled GPU for local model inference (Mistral 7B)  
- API key for Gemini (or other providers as needed)

### Install

git clone https://github.com/yourusername/myLLM.git
cd myLLM
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
Configure
Create a .env file in the root with your Gemini API key:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Add .env to .gitignore to keep your keys safe.

Run the API Server
bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 8000
Example Usage
python
Copy
Edit
import requests

response = requests.post("http://localhost:8000/v1/chat/completions", json={
    "model": "mistral",
    "messages": [
        {"role": "user", "content": "Hello, who are you?"}
    ]
})

print(response.json()['choices'][0]['message']['content'])
Adding Providers
Add your new provider in the providers/ folder, implement a completion(prompt: str) -> str function, then register it in router.py.

Future Roadmap
Streaming responses (server-sent events)

More model integrations (LLaMA, HuggingFace models, etc.)

Authentication & rate limiting

Web UI frontend

Document retrieval & RAG support

License
MIT License — feel free to use and modify!

Contributing
Contributions welcome! Please open issues or pull requests.

Contact
Created by NickelodeonOcom.
Feel free to reach out via GitHub issues or email.
