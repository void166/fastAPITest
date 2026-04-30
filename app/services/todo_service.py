from sqlalchemy.orm import Session
from app.crud import todo as crud
from app.schemas.todo import TodoCreate, TodoUpdate


class TodoService:
    """This class contains related todo actions"""

    def delete_todo(self, db: Session, todo_id: str):
        return crud.delete(db, todo_id)

    def create_todo(self, db: Session,user_id: str, todo: TodoCreate):
        return crud.create(db,user_id, todo)
    
    def get_all_todos(self, db: Session):
        return crud.get_all(db)
    
    def get_todo(self, db:Session, todo_id: str):
        return crud.get(db, todo_id)
    
    def get_todos_by_user_id(self, db: Session, user_id: str):
        return crud.getTodos_by_user_id(db, user_id)

    def mark_completed(self, db: Session, todo_id: str, completed: bool):
        return crud.update(db, todo_id, completed)
    
    def delete_todo(self, db: Session, todo_id: str):
        return crud.delete(db, todo_id)

    def update_todo(self, db: Session, todo_id: str, todo: TodoUpdate):
        obj = crud.get(db, todo_id)

        if not obj:
            return None

        if todo.title is not None:
            obj.title = todo.title

        if todo.description is not None:
            obj.description = todo.description

        if todo.completed is not None:
            obj.completed = todo.completed

        db.commit()
        db.refresh(obj)

        return obj


todo_service = TodoService()