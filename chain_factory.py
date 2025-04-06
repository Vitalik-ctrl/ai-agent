# chin_factory.py

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from memory import get_memory

def build_chain(llm, retriever, use_memory=True):
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that answers questions about the user's plans for 2025.\n\nContext:\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}")
    ])

    chain = (
        {
            "question": lambda x: x["question"],
            "chat_history": lambda x: x.get("chat_history", []),
            "context": lambda x: retriever.invoke(x["question"])
        }
        | prompt
        | llm
    )

    if use_memory:
        return RunnableWithMessageHistory(
            runnable=chain,
            get_session_history=get_memory,
            input_messages_key="question",
            history_messages_key="chat_history"
        )
    else:
        return chain
