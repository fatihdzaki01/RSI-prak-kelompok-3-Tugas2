from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, SmallInteger
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from src.database.schema.Registration import Registration

class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: int = Field(default=None, primary_key=True)

    name: str
    description: Optional[str] = None
    quota: int = Field(sa_column=Column(SmallInteger))

    started_at: datetime
    ended_at: datetime

    created_at: datetime = None
    updated_at: datetime = None

    registrations: list["Registration"] = Relationship(back_populates="event")
