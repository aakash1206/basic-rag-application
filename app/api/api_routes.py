from fastapi import APIRouter
from app.api.routes import question_answer
from app.api.routes import chatbot
from app.api.routes import rag_endpoints


api_router = APIRouter()


api_router.include_router(question_answer.router , prefix="/QA" , tags=["QA"])
api_router.include_router(chatbot.router , prefix="/bot" , tags=["bot"])
api_router.include_router(rag_endpoints.router , prefix="/rag" , tags=["rag"])
