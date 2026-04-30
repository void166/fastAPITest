from sqlalchemy import select
from app.models.todo import User
from app.crud.user import get
from app.core.security import create_access_token, hash_password, verify_password
from sqlalchemy.orm import Session







def create(db:Session, user: User):

    user.password = hash_password(user.password)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise e
        
    return user


def login(db: Session, email: str, password: str):
    user = db.execute(
        select(User).where(User.email == email)
        ).scalars().first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None
    
    token = create_access_token(
        email=user.email, 
        user_id=(user.id)
    )


    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": str(user.id),
        "email": user.email
    }
