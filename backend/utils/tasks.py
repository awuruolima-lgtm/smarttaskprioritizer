from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.db import get_db
from backend import schemas, models, crud
from backend.utils.nlp_parser import parse_human_date

router = APIRouter()

@router.post("/", response_model=schemas.TaskRead)
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, payload)

@router.post("/parse-create", response_model=schemas.TaskRead, summary="Create a task with human-readable due date (e.g., 'next Friday 5pm')")
def parse_and_create_task(payload: schemas.ParseAndCreateTask, db: Session = Depends(get_db)):
    due = parse_human_date(payload.human_due_date)
    create_payload = schemas.TaskCreate(
        name=payload.name,
        description=payload.description,
        category=payload.category,
        project=payload.project,
        status=payload.status,
        urgency=payload.urgency,
        importance=payload.importance,
        complexity=payload.complexity,
        due_date=due,
        estimated_minutes=payload.estimated_minutes,
    )
    return crud.create_task(db, create_payload)

@router.get("/", response_model=List[schemas.TaskRead])
def list_tasks(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: Optional[models.TaskStatus] = Query(None),
    category: Optional[str] = Query(None),
    project: Optional[str] = Query(None),
):
    return crud.get_tasks(db, skip=skip, limit=limit, status=status, category=category, project=project)

@router.get("/{task_id}", response_model=schemas.TaskRead)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/{task_id}", response_model=schemas.TaskRead)
def update_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, task, payload)

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task)
    return
