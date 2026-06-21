from langchain_core.prompts import PromptTemplate
from app.services.answer_parser import parser

prompt = PromptTemplate(
    template="""
Answer the user's question.

{format_instructions}

Question: {question}
""",
    input_variables=["question"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)