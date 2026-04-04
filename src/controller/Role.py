from fastapi import Depends
from sqlmodel import Session
from src.services.Role import RoleService
from src.database.connection import get_session
from src.dto.Role import RoleCreate

print(RoleService)
print(type(RoleService))
service = RoleService()


def get_roles(db: Session = Depends(get_session)):
    return service.get_roles(db)


def get_role(role_id: int, db: Session = Depends(get_session)):
    return service.get_role(db, role_id)


def create_role(data: RoleCreate, db: Session = Depends(get_session)):
    return service.create_role(db, data)


def update_role(role_id: int, data: RoleCreate, db: Session = Depends(get_session)):
    return service.update_role(db, role_id, data)


def delete_role(role_id: int, db: Session = Depends(get_session)):
    return service.delete_role(db, role_id)