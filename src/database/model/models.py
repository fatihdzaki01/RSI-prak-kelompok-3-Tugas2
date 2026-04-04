from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    first_name: str = Field(default=None, max_length=255)
    last_name: str = Field(default=None, max_length=255)
    whatsapp: str = Field(default=None, max_length=30)
    created_at: datetime = None
    updated_at: datetime = None

   # accounts: list["Account"] = Relationship(back_populates="user") --> nanti kalau udh ada punya angel
    #registrations: list["Registration"] = Relationship(back_populates="user")


