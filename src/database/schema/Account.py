from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime


class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str

    role_id: Optional[int] = Field(default=None, foreign_key="roles.id")

    role: Optional["Role"] = Relationship(back_populates="accounts")