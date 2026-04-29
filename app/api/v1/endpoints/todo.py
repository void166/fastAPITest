from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.todo import TodoCreate, TodoOut, TodoUpdate, TodoComplete
from app.services.todo_service import todo_service

router = APIRouter()


@router.post('/user/{user_id}', response_model= TodoOut)
def create(user_id: str,todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db,user_id, todo)


@router.get('/user/{user_id}', response_model=list[TodoOut])
def get_todos_by_user_id(user_id: str, db: Session = Depends(get_db)):
    return todo_service.get_todos_by_user_id(db, user_id)


@router.get('/', response_model=list[TodoOut])
def get_all_todos(db: Session = Depends(get_db)):
    return todo_service.get_all_todos(db)

@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: str, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(404, "not found")
    return todo

@router.patch("/{todo_id}", response_model=TodoOut)
def update(todo_id: str, data: TodoComplete, db: Session = Depends(get_db)):
    todo= todo_service.mark_completed(db, todo_id, data.completed)

    if not todo:
        raise HTTPException(404, "not found")
    
    return todo


@router.patch("/{todo_id}/details", response_model=TodoOut)
def update_details(todo_id: str, data: TodoUpdate, db: Session = Depends(get_db)):
    todo = todo_service.update_todo(db, todo_id, data)

    if not todo:
        raise HTTPException(404, "todo oldsongue")
    
    return todo

@router.delete("/{todo_id}")
def delete(todo_id: str, db: Session= Depends(get_db)):
    todo =  todo_service.delete_todo(db, todo_id)

    if not todo:
        raise HTTPException(404, "not found")
    
    return {
        "message": "todo deleted successfully",
        "todo_id": todo_id
    }
