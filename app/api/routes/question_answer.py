from fastapi import APIRouter
from app.schemas.question_schema import AskQuestionRequest
from app.services.ai_model import ask_question_ai_service


router = APIRouter()


@router.post("/ask-question")
def ask_question_controller(request :AskQuestionRequest):
    answer =  ask_question_ai_service(request.question)

    return {
        "data":answer ,
        "message" : "created"
    }