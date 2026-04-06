from sqlmodel import Session
from src.database.schema.Role import Role
from src.database.schema.Account import Account
from src.repositories.Account import AccountRepository
from datetime import datetime


class AccountService:

    def __init__(self):
        self.repo = AccountRepository()

    def get_accounts(self, db: Session):
        return self.repo.get_all(db)

    def get_account(self, db: Session, account_id: int):
        return self.repo.get_by_id(db, account_id)

    def create_account(self, db: Session, data):
        # validasi role
        role = db.get(Role, data.role_id)
        if not role:
            raise ValueError("role tidak ditemukan")
        existing = self.repo.get_by_user_id(db, data.user_id)
        if existing:
            raise ValueError("user sudah memiliki account")
    
        account = Account(**data.dict())
        return self.repo.create(db, account)

    def update_account(self, db: Session, account_id: int, data):
        account = self.repo.get_by_id(db, account_id)
        if not account:
            raise ValueError("account tidak ditemukan")

        if data.user_id is not None:
            account.user_id = data.user_id

        if data.role_id is not None:
            # validasi role
            role = db.get(Role, data.role_id)
            if not role:
                raise ValueError("role tidak ditemukan")
            account.role_id = data.role_id

        if data.email is not None:
            account.email = data.email

        if data.username is not None:
            account.username = data.username

        if data.password is not None:
            account.password = data.password

        account.updated_at = datetime.now()

        return self.repo.update(db, account)

    def delete_account(self, db: Session, account_id: int):
        account = self.repo.get_by_id(db, account_id)
        if not account:
            raise ValueError("account tidak ditemukan")

        self.repo.delete(db, account)
        return account