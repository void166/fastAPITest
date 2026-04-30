from sqlalchemy.orm import Session
from app.crud import user as crud


class UserService:


    """This class contains related user actions"""


    def update_user_password(self, db: Session, user_id: str, old_password: str, new_password: str):
        return crud.update_password(db, user_id, old_password, new_password)

    def delete_user(self, db: Session, user_id):
        return crud.delete(db, user_id)

    def get_all_users(self,db: Session):
        return crud.get_all(db)

    def get_user(self, db: Session, user_id):
        return crud.get(db, user_id)
    
user_service = UserService()





