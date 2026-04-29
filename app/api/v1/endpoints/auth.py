from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/login', response_model=str)
def login(payload: dict, db: Session = Depends(get_db)):
    email = payload.get("email")
    password = payload.get("password")

    if not email or not password:
        raise HTTPException(400, "email and password are required")
    
    user = crud.get_user_by_email(db, email)
    if not user or not user.verify_password(password):
        raise HTTPException(401, "invalid email or password")
    
    # Generate a token (for simplicity, using user ID as token here)
    token = generateToken(user.id, db)
    return token
