import os
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load .env automatically from project root
load_dotenv()

router = APIRouter()

# Get API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("DEBUG - Loaded API key:", OPENROUTER_API_KEY)

class ChatRequest(BaseModel):
    user_id: str
    query: str

@router.post("/chat")
def chat(request: ChatRequest):
    if not OPENROUTER_API_KEY:
        return {"error": "API key not found. Please set OPENROUTER_API_KEY in .env"}

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [{"role": "user", "content": request.query}],
            },
            timeout=30
        )

        if response.status_code != 200:
            return {"error": "Failed to connect to LLM", "details": response.text}

        data = response.json()
        answer = data["choices"][0]["message"]["content"]
        return {"reply": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
