from pydantic import BaseModel, UUID4

class TodoBase(BaseModel):
    owner_id: UUID4
    title: str
    description: str | None = None
    completed: bool = False

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TodoComplete(BaseModel):
    completed: bool

class TodoOut(TodoBase):
    id: UUID4

    class Config:
        from_attributes = True