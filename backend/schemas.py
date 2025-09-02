from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TaskCreate(BaseModel):
    name: str
    urgency: int
    importance: int
    complexity: int
    category: Optional[str] = "General"
    due_date: Optional[date]

class TaskResponse(TaskCreate):
    id: int
    priority_score: float

    class Config:
        orm_mode = True

class TaskList(BaseModel):
    tasks: List[TaskCreate]
