from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    accounts: list["Account"] = Relationship(back_populates="role")