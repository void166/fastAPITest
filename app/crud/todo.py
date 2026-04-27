from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate

def create(db:Session, todo:TodoCreate):
    obj= Todo(**todo.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all(db: Session):
    return db.query(Todo).all()

def get(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def delete(db: Session, todo_id: int):
    obj = get(db, todo_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def update(db: Session, todo_id: int, completed:bool):
    obj = get(db, todo_id)
    if obj:
        obj.completed = completed
        db.commit()
        db.refresh(obj)
    return obj

