from app.core.security import verify_access_token
from app.db.session import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    
    if not payload:
        raise HTTPException(401, "Invalid token")
    return payload




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()