from fastapi import APIRouter
from app.schemas.chatbot_schema import ChatbotRequest
from app.services.chat_service.chatbot_service import chatbot_service


router = APIRouter()


@router.post('/query')
def chat_bot_controller(request :ChatbotRequest ):
    print(request.query)

    res = chatbot_service(request)

    return {
        "response" : res
    }