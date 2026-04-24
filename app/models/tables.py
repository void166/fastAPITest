from sqlalchemy import Column, BigInteger, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    full_name = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")

class Todo(Base):
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    content = Column(Text(), nullable=False)
    is_completed = Column(Boolean(), nullable=False, default=False)
    category = Column(String(50), nullable=True)
    priority = Column(String(20), nullable=True)

    # ForeignKey
    created_by_id = Column(GUID, ForeignKey('user.id'), nullable=False)

    # Relationship
    owner = relationship("User", back_populates="todos")

    def dict(self):
        return super().dict()