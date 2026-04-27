from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.todo import User

def create(db:Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete(db:Session, user_id: str):
    obj = get(db, user_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj



def get_all(db: Session):
    return db.execute(select(User)).scalars().all()

def get(db: Session, user_id: str):
    return db.execute(select(User).where(User.id == user_id)).scalars().first()

def get_by_username(db: Session, username: str):
    return db.execute(select(User).where(User.username == username)).scalars().first()



