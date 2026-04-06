from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.database.schema.Role import Role
from src.database.schema.User import User


class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id")
    role_id: int = Field(foreign_key="roles.id")

    email: str
    username: str = Field(default=None, max_length=16)
    password: str

    created_at: datetime = None
    updated_at: datetime = None

    user: Optional[User] = Relationship(back_populates="accounts")
    role: Optional[Role] = Relationship(back_populates="accounts")
