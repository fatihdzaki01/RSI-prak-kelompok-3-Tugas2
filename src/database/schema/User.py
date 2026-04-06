from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.database.schema.Registration import Registration

if TYPE_CHECKING:
    from src.database.schema.Account import Account


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=255)
    last_name: str = Field(default=None, max_length=255)
    whatsapp: str = Field(default=None, max_length=30)
    created_at: datetime = None
    updated_at: datetime = None
    registrations: list["Registration"] = Relationship(back_populates="user")
    accounts: list["Account"] = Relationship(back_populates="user")
