from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session



from app.api.deps import get_db
from app.schemas.User import UserCreate, UserOut
from app.services import user_service
from app.crud import user as crud

router= APIRouter()

@router.post('/register', response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/users', response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.get('/users/{user_id}', response_model=UserOut)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(404, "not found")
    return user

@router.delete('/users/{user_id}')
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(404, "not found")
    user_service.delete_user(db, user_id)
    return {"message": "User deleted successfully"}
