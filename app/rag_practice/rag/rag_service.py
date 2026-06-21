from app.rag_practice.retrieval.retrieval_service import RetrievalService
from app.rag_practice.llm.huggingface_llm import HuggingFaceLLM
import re


class RAGService:

    @staticmethod
    def ask(question: str):
        docs = RetrievalService.retrieve(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
        You are a helpful assistant.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        llm = HuggingFaceLLM().get_llm()

        response = llm.invoke(prompt).content

        clean_answer = re.sub(r"\s+", " ", response).strip()

        return clean_answer