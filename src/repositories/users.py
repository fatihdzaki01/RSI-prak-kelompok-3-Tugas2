from sqlmodel import Session, select
from src.database.model.models import User


class UsersRepository:

    def get_all(self, db: Session):
        return db.exec(select(User)).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.get(User, user_id)

    def create(self, db, user):
        db_user = User(**user.dict())  # convert di sini
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def update(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user: User):
        db.delete(user)
        db.commit()