import uuid
from pydantic import EmailStr
from fastapi_users import schemas

class UserRead(schemas.BaseUser[uuid.UUID]):
    email: EmailStr
    is_superUser:bool

class userCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str


class userUpdate(schemas.BaseUserUpdate):
    password: str