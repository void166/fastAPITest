from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session



from app.api.deps import get_db
from app.schemas.User import UserCreate, UserOut, UserPasswordUpdate
from app.services.user_service import user_service

router= APIRouter()


@router.put('/users/{user_id}/password', response_model=UserOut)
def update_password(user_id: str, payload: UserPasswordUpdate, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)

    if not user:
        raise HTTPException(404, "user not found")
    
    updated_user = user_service.update_user_password(db, user_id, payload.old_password, payload.new_password)

    if not updated_user:
        raise HTTPException(400, "old password is incorrect")
    
    return updated_user

@router.post('/register', response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/users', response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)


# todonuud tei ni gargay
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
