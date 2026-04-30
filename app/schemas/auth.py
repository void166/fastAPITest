from pydantic import BaseModel


class AuthLogin(BaseModel):
    email: str
    password: str

class AuthRegister(AuthLogin):
    username: str
    gender: str | None = None
    age: int | None =None
    address: str | None = None
