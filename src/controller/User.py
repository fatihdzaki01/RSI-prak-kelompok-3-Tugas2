from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.database.connection import get_session
from src.dto.User import UserCreate
from src.services.User import UsersService

service = UsersService()


def get_users(db: Session = Depends(get_session)):
    try:
        return service.get_all_users(db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_user(user_id: int, db: Session = Depends(get_session)):
    try:
        return service.get_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def create_user(data: UserCreate, db: Session = Depends(get_session)):
    try:
        return service.create_user(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_session)):
    try:
        return service.update_user(db, user_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def delete_user(user_id: int, db: Session = Depends(get_session)):
    try:
        return service.delete_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
