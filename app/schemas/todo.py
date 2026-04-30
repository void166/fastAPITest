from pydantic import BaseModel, UUID4
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    priority: str = "medium"
    due_date: datetime | None = None


class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    priority: str = "medium"
    due_date: datetime | None = None


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: str | None = None
    due_date: datetime | None = None


class TodoComplete(BaseModel):
    completed: bool


class TodoOut(TodoBase):
    id: UUID4
    owner_id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True