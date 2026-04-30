from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.todo import User
from app.core.security import hash_password, verify_password


def update_password(db: Session, user_id: str, old_password: str, new_password: str):
    try:
        user = get(db, user_id)
        if user and verify_password(old_password, user.password):
            user.password = hash_password(new_password)
            db.commit()
            db.refresh(user)
            return user
        return None
    except Exception as e:
        db.rollback()
        raise e

def delete(db:Session, user_id: str):
    try:
        obj = get(db, user_id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj
    except Exception as e:
        db.rollback()
        raise e



def get_all(db: Session):
    return db.execute(select(User)).scalars().all()

def get(db: Session, user_id: str):
    return db.execute(select(User).where(User.id == user_id)).scalars().first()

def get_by_email(db: Session, email: str):
    return db.execute(select(User).where(User.email == email)).scalars().first()



