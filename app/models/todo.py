from datetime import datetime
from app.core.security import verify_password
from sqlalchemy import Column, Enum, String, Boolean, ForeignKey, DateTime,Integer, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)

    completed = Column(Boolean, default=False)

    priority = Column(
        Enum('low', 'medium', 'high', name='priority_enum'), 
        default='medium'
    )

    due_date = Column(DateTime, nullable=True)

    owner_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='CASCADE')
    )

    owner  = relationship("User", back_populates="todos")

    created_at = Column(DateTime, server_default=func.now())


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    address = Column(String, nullable=True)

    todos = relationship("Todo", back_populates="owner")

    created_at = Column(DateTime, server_default=func.now())
    

    def verify_password(self, plain_password: str) -> bool:
        return verify_password(plain_password, self.password)