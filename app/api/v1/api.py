from fastapi import APIRouter
from app.api.v1.endpoints import todo, user

api_router = APIRouter()
api_router.include_router(todo.router, prefix="/todos", tags=["todos"])
api_router.include_router(user.router, prefix="", tags=["users"])
