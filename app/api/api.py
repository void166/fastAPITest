from fastapi import APIRouter
from app.api import api_todo
from app.api import api_user
from app.api import api_auth
from app.db.deps import get_current_user
from fastapi import Depends

api_router = APIRouter()


api_router.include_router(
    api_todo.router,
    prefix="/todos",
    tags=["todos"],
    dependencies=[Depends(get_current_user)]
)
api_router.include_router(
    api_user.router, 
    prefix="/users", 
    tags=["users"]
)
api_router.include_router(
    api_auth.router,
    prefix="/auth",
    tags=["auth"]
)