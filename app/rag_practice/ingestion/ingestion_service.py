import os
import uuid
from fastapi import UploadFile , HTTPException
from app.rag_practice.loaders.pdf_loader import PDFLoader
from app.rag_practice.chunkers.recursive_chunker import RecursiveChunker
from app.rag_practice.embeddings.huggingface_embedding import MyHuggingFaceEmbedding
from langchain_community.vectorstores import FAISS

UPLOAD_DIR = "storage/uploads"
FAISS_DIR = "storage/faiss_index"

class IngestionService:

    @staticmethod
    async def process_pdf(file: UploadFile):

        # Validate PDF
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed"
            )

        # Create folders
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        os.makedirs(FAISS_DIR, exist_ok=True)

        # Generate unique filename
        extension = os.path.splitext(file.filename)[1]

        unique_filename = f"{uuid.uuid4()}{extension}"

        file_path = os.path.join(
            UPLOAD_DIR,
            unique_filename
        )

        try:

            # Save PDF
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())

            # Load PDF
            documents = PDFLoader.loader(file_path)


    
            # Chunking
            chunks = RecursiveChunker.chunk_documents(documents)

        

            
            # Embeddings

            embedding = MyHuggingFaceEmbedding().embedding_model
    

            # Create FAISS Vector Store

            vector_store = FAISS.from_documents(
                documents=chunks,
                embedding=embedding
            )


            
           
            # Save FAISS Index

            vector_store.save_local(FAISS_DIR)
           
            return {
                "message": "PDF indexed successfully",
                "filename": file.filename,
                "stored_filename": unique_filename,
                "total_pages": len(documents),
                "total_chunks": len(chunks)
            }

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
    