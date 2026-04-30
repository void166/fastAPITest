from app.crud.auth import login 
from app.models.todo import User
from app.crud import auth as auth_crud
from app.crud import user as user_crud
from app.schemas.auth import UserRegister
from sqlalchemy.orm import Session

class AuthService:
    """Authentication service for handling user login and token generation."""
    

    def create_user(self, db: Session, user: UserRegister):
        db_user = user_crud.get_by_email(db, user.email)
        if db_user:
            raise ValueError("email already registered")
        
        user_data = user.model_dump()
     
        return auth_crud.create(db, User(**user_data))
    
    
    @staticmethod
    def login(db: Session, email: str, password: str):
        return login(db, email, password)
    

AuthService = AuthService();
    
