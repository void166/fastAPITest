from pydantic import BaseModel, UUID4

class UserBase(BaseModel):
    email: str
    username: str
    password: str


class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: UUID4

    class Config:
        from_attributes = True

