from fastapi import APIRouter, UploadFile, File, HTTPException
from app.rag_practice.ingestion.ingestion_service import IngestionService
from app.rag_practice.rag.rag_service import RAGService

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf_controller(file: UploadFile = File(...)):
    
    try:
              return await IngestionService.process_pdf(file)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


from fastapi import Query

@router.post("/ask")
def ask_question(question: str = Query(...)):
    print(question)

    answer = RAGService.ask(question)

    return {
        "answer": answer
    }