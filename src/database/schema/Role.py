from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database.schema.Account import Account

class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    accounts: list["Account"] = Relationship(back_populates="role")