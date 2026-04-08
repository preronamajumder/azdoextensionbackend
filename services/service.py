from datetime import datetime

def generate_response(question: str) -> str:
    q = question.lower()

    if "bug" in q:
        return "There are 3 open bugs in the system."
    elif "task" in q:
        return "You have 5 active tasks."
    elif "time" in q:
        return f"Current server time is {datetime.now().strftime('%H:%M:%S')}."
    elif "status" in q:
        return "All systems are operational."
    else:
        return f"Received your query: '{question}'. Backend is working correctly."