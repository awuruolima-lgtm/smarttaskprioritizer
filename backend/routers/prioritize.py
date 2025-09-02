from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, db

router = APIRouter()

@router.post("/prioritize", response_model=list[schemas.TaskResponse])
def prioritize_tasks(task_list: schemas.TaskList, db: Session = Depends(db.get_db)):
    created_tasks = crud.create_tasks_bulk(db, task_list.tasks)
    return created_tasks
