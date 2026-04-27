from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.todo import TodoCreate, TodoOut, TodoUpdate
from app.services import todo_service
from app.crud import todo as crud

router = APIRouter()

@router.get('/user/{user_id}', response_model=list[TodoOut])
def get_todos_by_user_id(user_id: str, db: Session = Depends(get_db)):
    return crud.getTodos_by_user_id(db, user_id)

@router.post('/', response_model= TodoOut)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)

@router.get('/', response_model=list[TodoOut])
def real_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

@router.get("/{todo_id}", response_model=TodoOut)
def read_one(todo_id: str, db: Session = Depends(get_db)):
    todo = crud.get(db, todo_id)
    if not todo:
        raise HTTPException(404, "not found")
    return todo

@router.put("/{todo_id}", response_model=TodoOut)
def update(todo_id: str, data: TodoUpdate, db: Session = Depends(get_db)):
    return todo_service.mark_completed(db, todo_id, data.completed)

@router.delete("/{todo_id}")
def delete(todo_id: str, db: Session= Depends(get_db)):
    return crud.delete(db, todo_id)
