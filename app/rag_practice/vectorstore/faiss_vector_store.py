from langchain_community.vectorstores import FAISS


class FaissVectorStore:
    @staticmethod
    def create_vector_store(documents, embeddings):
        vector_store = FAISS.from_documents(
            documents=documents,
            embedding=embeddings
        )
        return vector_store