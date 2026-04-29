from sqlalchemy.orm import Session
from app.models.todo import User
from app.crud import user as crud
from app.schemas.User import UserCreate




class UserService:


    """This class contains related user actions"""
    
    def create_user(self, db: Session, user: UserCreate):
        db_user = crud.get_by_email(db, user.email)
        if db_user:
            raise ValueError("email already registered")
        
        user_data = user.model_dump()
     
        return crud.create(db, User(**user_data))
    
    def update_user_password(self, db: Session, user_id: str, old_password: str, new_password: str):
        return crud.update_password(db, user_id, old_password, new_password)


    def delete_user(self, db: Session, user_id):
        return crud.delete(db, user_id)

    def get_all_users(self,db: Session):
        return crud.get_all(db)

    def get_user(self, db: Session, user_id):
        return crud.get(db, user_id)
    
user_service = UserService()





