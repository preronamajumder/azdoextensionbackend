from datetime import datetime

def generate_response(question: str) -> str:
    q = question.lower()
    
    if "bug" in q:
        return "question: "+ question + "\nThere are 3 open bugs in the system."
    elif "task" in q:
        return "question: "+ question + "\nYou have 5 active tasks."
    elif "time" in q:
        return "question: "+ question + f"\nCurrent server time is {datetime.now().strftime('%H:%M:%S')}."
    elif "status" in q:
        return "question: "+ question + "\nAll systems are operational."
    else:
        return f"Received your query: '{question}'. Backend is working correctly."