from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(UserLogin):
    username: str
    gender: str | None = None
    age: int | None =None
    address: str | None = None
