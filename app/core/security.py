from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)-> bool:
    return pwt_context.verify(plain_password, hashed_password);


def generate_token(email: str, user_id: str, algorithm: str, expire_minutes: int):

    secret_key = settings.JWT_SECRET_KEY

    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    to_encode = {"sub": email, "user_id": user_id, "exp": expire}
    token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return token
