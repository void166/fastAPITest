from sqlalchemy.orm import Session
from app.models.todo import User
from app.crud import user as crud
from app.schemas.User import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = crud.get_by_email(db, user.email)
    if db_user:
        raise ValueError("email already registered")
    return crud.create(db, User(**user.dict()))

def delete_user(db: Session, user_id):
    return crud.delete(db, user_id)

def get_all_users(db: Session):
    return crud.get_all(db)

def get_user(db: Session, user_id):
    return crud.get(db, user_id)

