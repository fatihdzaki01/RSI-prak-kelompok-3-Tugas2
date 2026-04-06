from sqlmodel import Session, select

from src.database.schema.Account import Account


class AccountRepository:
    def get_all(self, db: Session):
        return db.exec(select(Account)).all()

    def get_by_id(self, db: Session, account_id: int):
        return db.get(Account, account_id)

    def create(self, db: Session, account: Account):
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def update(self, db: Session, account: Account):
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def delete(self, db: Session, account: Account):
        db.delete(account)
        db.commit()

    def get_by_user_id(self, db: Session, user_id: int):
        statement = select(Account).where(Account.user_id == user_id)
        return db.exec(statement).first()
