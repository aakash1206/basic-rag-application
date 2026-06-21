from dotenv import load_dotenv
import os

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace
)

load_dotenv()


class HuggingFaceLLM:

    @staticmethod
    def get_llm():

        llm = HuggingFaceEndpoint(
            repo_id="meta-llama/Llama-3.1-8B-Instruct",
            huggingfacehub_api_token=os.getenv(
                "HUGGING_FACE_TOKEN"
            ),
            max_new_tokens=256,
            temperature=0
        )

        return ChatHuggingFace(llm=llm)