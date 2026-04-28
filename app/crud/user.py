from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.todo import User
from app.core.security import hash_password

def create(db:Session, user: User):

    user.password = hash_password(user.password)


    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db: Session, email: str, password: str):
    user = db.execute(select(User).where(User.email == email)).scalars().first()
    if user and user.verify_password(password):
        return user
    return None

def updatePassword(db: Session, user_id: str, old_password: str, new_password: str):
    user = get(db, user_id)
    if user and user.verify_password(old_password):
        user.password = hash_password(new_password)
        db.commit()
        db.refresh(user)
        return user
    return None

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

def get_by_email(db: Session, email: str):
    return db.execute(select(User).where(User.email == email)).scalars().first()



