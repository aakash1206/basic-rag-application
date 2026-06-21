from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from app.services.prompt import prompt
from app.services.answer_parser import parser

load_dotenv()



repo_id="meta-llama/Llama-3.1-8B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
  
    huggingfacehub_api_token=os.getenv("HUGGING_FACE_TOKEN")
)

chat_model = ChatHuggingFace(llm=llm)


chain = prompt | chat_model |parser

def ask_question_ai_service(question: str) -> str:
    try:
     

        response = chain.invoke(question)
       
        return response

    except Exception as e:
        print("HF ERROR:", str(e))
        return "Sorry, AI service failed"