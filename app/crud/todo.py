from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.todo import Todo
from app.schemas.todo import TodoCreate

def create(db:Session,user_id: str, todo:TodoCreate):
    
    obj= Todo(**todo.model_dump(), owner_id=user_id)

    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
    except Exception as e:
        db.rollback()
        raise e
    return obj


def getTodos_by_user_id(db: Session,user_id):
    return db.execute(select(Todo).where(Todo.owner_id == user_id)).scalars().all()


def get_all(db: Session):
    return db.execute(select(Todo)).scalars().all()

def get(db: Session, todo_id: str):
    return db.execute(select(Todo).where(Todo.id == todo_id)).scalars().first()

def delete(db: Session, todo_id: str):

    try:
        obj = get(db, todo_id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj
    except Exception as e:
        db.rollback()
        raise e


def update(db: Session, todo_id: str, completed:bool):
    try:
        obj = get(db, todo_id)
        if obj:
            obj.completed = completed
            db.commit()
            db.refresh(obj)
        return obj
    except Exception as e:
        db.rollback()
        raise e

