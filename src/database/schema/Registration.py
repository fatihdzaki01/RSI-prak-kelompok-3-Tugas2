from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.database.schema.Event import Event
    from src.database.schema.User import User


class Registration(SQLModel, table=True):
    __tablename__ = "registrations"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    event_id: int = Field(foreign_key="events.id")

    user: Optional["User"] = Relationship(back_populates="registrations")
    event: Optional["Event"] = Relationship(back_populates="registrations")
