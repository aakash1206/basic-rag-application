from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


prompt = ChatPromptTemplate.from_messages([
("system", "You are a helpful assistant"),
MessagesPlaceholder(variable_name="history"),
("human", "{question}")
])


