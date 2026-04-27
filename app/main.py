from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.api import api_router

Base.metadata.create_all(bind=engine)

app=FastAPI(title="todo API")

app.include_router(api_router, prefix="/api/v1")