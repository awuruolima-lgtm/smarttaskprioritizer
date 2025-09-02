from sqlalchemy.orm import Session
from . import models, schemas
from .services.prioritizer import calculate_priority

def create_task(db: Session, task: schemas.TaskCreate):
    task_dict = task.dict()
    task_dict["priority_score"] = calculate_priority(task_dict)
    db_task = models.Task(**task_dict)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def create_tasks_bulk(db: Session, tasks: list[schemas.TaskCreate]):
    results = []
    for task in tasks:
        results.append(create_task(db, task))
    return results

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

