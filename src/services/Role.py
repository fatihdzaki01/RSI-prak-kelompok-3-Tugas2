from sqlmodel import Session
from src.repositories.Role import RoleRepository
from src.database.schema.Role import Role
from datetime import datetime


class RoleService:

    def __init__(self):
        self.repo = RoleRepository()

    def get_roles(self, db: Session):
        return self.repo.get_all(db)

    def get_role(self, db: Session, role_id: int):
        role = self.repo.get_by_id(db, role_id)
        if not role:
            raise ValueError("role tidak ditemukan")
        return role
    
    def create_role(self, db: Session, data):
        role = Role(
            **data.dict()
        )
        return self.repo.create(db, role)

    def update_role(self, db: Session, role_id: int, data):
        role = self.repo.get_by_id(db, role_id)
        if not role:
            raise ValueError("role tidak ditemukan")

        role.name = data.name

        return self.repo.update(db, role)

    def delete_role(self, db: Session, role_id: int):
        role = self.repo.get_by_id(db, role_id)
        if not role:
            raise ValueError("role tidak ditemukan")

        self.repo.delete(db, role)
        return role