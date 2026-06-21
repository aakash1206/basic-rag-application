from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class RecursiveChunker:

    @staticmethod
    def chunk_documents(documents: list[Document]):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        return text_splitter.split_documents(documents)