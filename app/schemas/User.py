from datetime import datetime

from pydantic import BaseModel, UUID4, Field

from app.schemas.todo import TodoOut


class UserList(BaseModel):
    email: str
    username: str
    gender: str | None = None
    age: int | None = None
    address: str | None = None


class UserPasswordUpdate(BaseModel):
    old_password: str
    new_password: str


class UserOut(UserList):
    id: UUID4
    created_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }


class User(UserOut):
    todos: list[TodoOut] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }