from pydantic import BaseModel, UUID4

class TodoBase(BaseModel):
    owner_id: UUID4
    title: str
    description: str | None = None
    completed: bool = False

class TodoCreate(BaseModel):
    owner_id: UUID4
    title: str
    description: str | None = None
    completed: bool = False

class TodoUpdate(BaseModel):
    owner_id: UUID4
    todo_id: UUID4
    title: str | None = None
    description: str | None = None
    completed: bool

class TodoOut(TodoBase):
    id: UUID4

    class Config:
        from_attributes = True