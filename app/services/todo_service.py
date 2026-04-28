from sqlalchemy.orm import Session
from app.crud import todo as crud
from app.schemas.todo import TodoCreate

def create_todo(db: Session, todo: TodoCreate):
    return crud.create(db, todo)

def mark_completed(db: Session, todo_id: int, completed: bool):
    return crud.update(db, todo_id, completed)

def update_todo(db: Session, todo_id: str, todo: TodoCreate):
    obj = crud.get(db, todo_id)
    if obj:
        obj.title = todo.title
        obj.description = todo.description
        db.commit()
        db.refresh(obj)
    return obj
