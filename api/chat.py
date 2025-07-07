from fastapi import APIRouter
from models import ChatRequest
from router import route

router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completion(request: ChatRequest):
    prompt = "\n".join([f"{m.role}: {m.content}" for m in request.messages])
    model_fn = route(request.model)
    reply = model_fn(prompt)
    return {
        "choices": [{"message": {"role": "assistant", "content": reply}}],
        "model": request.model
    }

