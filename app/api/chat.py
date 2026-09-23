from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot import chatbot

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(request: ChatRequest):
    result = chatbot.invoke({
        "message": request.message,
        "response": ""
    })

    return {
        "message": request.message,
        "response": result["response"]
    }