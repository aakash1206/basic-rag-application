from langchain_huggingface import HuggingFaceEmbeddings

class MyHuggingFaceEmbedding:

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    ):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=model_name
        )

    def embed_documents(self, documents):
        return self.embedding_model.embed_documents(documents)

    def get_embedor(self):
        return self.embedding_model

    def embed_query(self, query: str):
        return self.embedding_model.embed_query(query)