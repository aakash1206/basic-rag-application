from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Answer(BaseModel):
    question: str = Field(description="User question")
    answer: str = Field(description="AI generated answer")



parser = PydanticOutputParser(pydantic_object=Answer)
