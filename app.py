# app.py

import os
import re

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from load_docs import load_vectorstore
from chain_factory import build_chain
from agent_factory import build_agent
from memory import save_history
from executor import execute_command
from config import session_id

load_dotenv()
api_key = os.getenv("GEMINI_KEY")

vectorstore = load_vectorstore(["plans2025.txt", "chat_history.txt"], api_key)
retriever = vectorstore.as_retriever()
agent = build_agent(retriever)

print("\nAsk anything. (type 'exit' to quit)\n")

while True:
    
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    
    result = agent.invoke(
        {"input": query}, 
        config={
            "configurable": {"session_id": session_id},
            "return_intermediate_steps": True}
    )
    
    print(f"AI: {result['output']}\n")
    #execute_command(result['intermediate_steps'][-1]['message']['content'])

        
    for action, tool_output in result.get("intermediate_steps", []):

        if action.tool == "create_terminal_command" and "[COMMAND_PENDING]:" in tool_output:
            match = re.search(r"\[COMMAND_PENDING\]:(.+?)(\{|$)", tool_output)
            if match:
                command = match.group(1).strip()
                execute_command(command)

save_history(session_id, "chat_history.txt")
