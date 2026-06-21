from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from app.schemas.chatbot_schema import ChatbotRequest
from app.services.chat_service.chat_history_prompt import prompt
from langchain_core.output_parsers import StrOutputParser
# from langchain.memory import ConversationBufferMemory
from langchain_classic.memory import ConversationBufferMemory



load_dotenv()



repo_id="meta-llama/Llama-3.1-8B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=os.getenv("HUGGING_FACE_TOKEN")
)



model = ChatHuggingFace(llm = llm)

memory = ConversationBufferMemory(return_messages=True)


chain = prompt | model | StrOutputParser()


# def chatbot_service(queryRequest : ChatbotRequest) :

#     res = chain.invoke({
#         "question":history,
#         "history" : queryRequest.query
#         })
    


#     print(res)
#     print(queryRequest.query)




def chatbot_service(queryRequest):




    res = chain.invoke({
        "question": queryRequest.query,
        "history": memory.load_memory_variables({})["history"]
    })

  

    memory.save_context(
        {"question": queryRequest.query},
        {"output": res}
    )

    return res