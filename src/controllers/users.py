from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.database.db import get_session
from src.services.users import UsersService
from src.database.model.models import User

router = APIRouter()
service = UsersService()

@router.get("/users")
def get_users(db: Session = Depends(get_session)):
    return service.get_all_users(db)

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_session)):
    return service.get_user(db, user_id)

@router.post("/users")
def create_user(user: User, db: Session = Depends(get_session)):
    return service.create_user(db, user)

@router.put("/users/{user_id}")
def update_user(user_id: int, user: User, db: Session = Depends(get_session)):
    user.id = user_id
    return service.update_user(db, user)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_session)):
    user = service.get_user(db, user_id)
    return service.delete_user(db, user)