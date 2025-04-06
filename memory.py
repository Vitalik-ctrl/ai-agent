# memory.py

from langchain_community.chat_message_histories import ChatMessageHistory

session_memory = {}

def get_memory(session_id: str):
    if session_id not in session_memory:
        session_memory[session_id] = ChatMessageHistory()
    return session_memory[session_id]

def save_history(session_id: str, file_path: str):
    if session_id in session_memory:
        history = session_memory[session_id]
        with open(file_path, 'w') as f:
            f.write(str(history))
    else:
        print(f"No history found for session ID: {session_id}")
        