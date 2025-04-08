# app.py

import os
import re

from dotenv import load_dotenv
from load_docs import load_vectorstore
from agent_factory import build_agent
from memory import save_history
from executor import execute_command
from config import session_id

load_dotenv()
api_key = os.getenv("GEMINI_KEY")

files = [os.path.join("local_knowledge_base", f) for f in os.listdir("local_knowledge_base") 
         if os.path.isfile(os.path.join("local_knowledge_base", f))]

vectorstore = load_vectorstore(files, api_key)
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
            "return_intermediate_steps": True
            }
    )

    print(f"AI: {result['output']}\n")

    for action, tool_output in result.get("intermediate_steps", []):

        if action.tool == "create_terminal_command" and "[COMMAND_PENDING]:" in tool_output:
            match = re.search(r"\[COMMAND_PENDING\]:(.+?)(\{|$)", tool_output)
            if match:
                command = match.group(1).strip()
                print(execute_command(command))

save_history(session_id, "local_knowledge_base/last_chat_history.txt")
