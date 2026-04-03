from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.database.schema.Event import Event

# from src.database.schema.User import User


class Registration(SQLModel, table=True):
    __tablename__ = "registrations"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None)
    event_id: int = Field(default=None, foreign_key="events.id")

    # user: Optional[User] = Relationship(back_populates="registrations") karena punya acid blm kelar
    event: Optional[Event] = Relationship(back_populates="registrations")
