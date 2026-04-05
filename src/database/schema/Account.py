from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from src.database.schema.Role import Role
from src.database.schema.User import User

class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: int = Field(default=None, primary_key=True)

    user_id: int = Field(default=None, foreign_key="users.id")
    role_id: int = Field(default=None, foreign_key="roles.id")

    email: str = None
    username: str = Field(default=None, max_length=16)
    password: str = None

    created_at: datetime = None
    updated_at: datetime = None

    user: Optional[User] = Relationship(back_populates="accounts")
    role: Optional[Role] = Relationship(back_populates="accounts")