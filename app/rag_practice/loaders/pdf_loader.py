from langchain_community.document_loaders import PyMuPDFLoader

class PDFLoader:
    @staticmethod
    def loader(file_path:str):
        loader = PyMuPDFLoader(file_path=file_path)
        return loader.load()