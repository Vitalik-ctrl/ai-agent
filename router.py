def route_input(user_input: str) -> str:
    lower = user_input.lower()

    if "time" in lower or "date" in lower or "now" in lower:
        return "agent"

    if "summary" in lower:
        return "summary"

    return "rag" 
