from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: int = Field(default=None, primary_key=True)

    name: str = None
    description: str = None
    quota: int = None

    started_at: datetime = None
    ended_at: datetime = None

    created_at: datetime = None
    updated_at: datetime = None

    registrations: list["Registration"] = Relationship(back_populates="event")
