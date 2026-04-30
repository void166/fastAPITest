from app.db.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.auth import UserLogin, UserRegister
from app.schemas.User import UserOut
from app.services.auth_service import AuthService


router = APIRouter()

@router.post('/register', response_model=UserOut)
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        return AuthService.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = AuthService.login(db, form_data.username, form_data.password)
    if not result:
        raise HTTPException(400, "invalid email or password")
    
    return result