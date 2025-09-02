from ..schemas import TaskCreate

def calculate_priority(task: TaskCreate, weights: dict = None) -> float:
    if not weights:
        weights = {"urgency": 1.0, "importance": 1.0, "complexity": 0.5}
    score = (
        task.urgency * weights["urgency"]
        + task.importance * weights["importance"]
        - task.complexity * weights["complexity"]
    )
    return round(score, 2)
