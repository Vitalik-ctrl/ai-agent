# agent_factory.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from tools import get_current_time as time_tool, search as search_tool, create_terminal_command as terminal_tool
from tools import init_rag_tool
from memory import get_memory

load_dotenv()

def build_agent(retriever):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=os.getenv("GEMINI_KEY")
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. If the user asks about their info or anything you possibly cannot know, use the RAG tool to answer. If there is no relevant information, say 'I don't know'"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}") 
    ])

    rag_tool = init_rag_tool(retriever)
    tools = [time_tool, search_tool, terminal_tool, rag_tool]

    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    return RunnableWithMessageHistory(
        runnable=AgentExecutor(
            agent=agent,
            tools=tools,
            return_intermediate_steps=True,
            verbose=False # Set verbose on True to allow debug info printed
        ),
        get_session_history=get_memory,
        input_messages_key="input",            
        history_messages_key="chat_history"    
    )
    