import os
from langchain_community.vectorstores import FAISS
from app.rag_practice.embeddings.huggingface_embedding import MyHuggingFaceEmbedding
from app.rag_practice.ingestion.ingestion_service import FAISS_DIR

class RetrievalService:

    @staticmethod
    def retrieve(question: str):

       
        embedding_model = (
            MyHuggingFaceEmbedding()
            .embedding_model
        )

        vector_store = FAISS.load_local(
            folder_path=FAISS_DIR,
            embeddings=embedding_model,
            allow_dangerous_deserialization=True
        )

        documents = vector_store.similarity_search(
            query=question,
            k=3
        )

        return documents