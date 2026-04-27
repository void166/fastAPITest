from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    descrion: str | None = None
    completed: bool

class TodoOut(TodoBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True