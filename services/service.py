from datetime import datetime

def generate_response(question: str, work_item_id: str, title: str, description: str) -> str:
    q = question.lower()
    
    # if "bug" in q:
    #     return "There are 3 open bugs in the system."
    # elif "task" in q:
    #     return "You have 5 active tasks."
    # elif "time" in q:
    #     return f"\nCurrent server time is {datetime.now().strftime('%H:%M:%S')}."
    # elif "status" in q:
    #     return "All systems are operational."
    # else:
    #     return f"Received your query: '{question}'. Backend is working correctly."
    
    if "id" in q:
        return f"The work item ID is {work_item_id}."
    elif "title" in q:
        return f"The title is {title}."
    elif "description" in q:
        return f"The description is {description}."
    else:
        return f"Received your query: '{question}'. Backend is working correctly."