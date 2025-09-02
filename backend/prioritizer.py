def calculate_priority(task: dict):
    """
    Calculate priority score based on weighted formula:
    priority_score = (urgency * 0.5 + importance * 0.5) / complexity
    """
    urgency = task.get("urgency", 1)
    importance = task.get("importance", 1)
    complexity = task.get("complexity", 1) or 1  # avoid division by zero
    score = (urgency * 0.5 + importance * 0.5) / complexity
    return round(score, 2)
