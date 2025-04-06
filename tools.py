# tools.py

from langchain.tools import tool
from datetime import datetime
from duckduckgo_search import DDGS


@tool
def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def search(query: str) -> str:
    """Search the web using DuckDuckGo and return the top result."""
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            top_result = next(iter(results), None) 
            if top_result:
                return f"{top_result['title']}\n{top_result['href']}\n{top_result['body']}"
            else:
                return "No results found."
    except Exception as e:
        return f"An error occurred during search: {e}"
    
@tool
def create_terminal_command(command: str) -> str:
    """Create a terminal command and return it."""
    return f"[COMMAND_PENDING]:{command}"

def init_rag_tool(retriever):
    @tool
    def retriveal_augmented_generation(query: str) -> str:
        """Retrieve relevant documents with user personal information and generate a response using RAG."""
        try:
            context = retriever.invoke(query)
            if not context:
                return "No relevant information found."
            return context[0].page_content
        except Exception as e:
            return f"An error occurred during retrieval: {e}"
    return retriveal_augmented_generation