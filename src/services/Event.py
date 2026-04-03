from datetime import datetime

from sqlmodel import Session

from src.database.schema.Event import Event
from src.repositories.Event import EventRepository


class EventService:
    def __init__(self):
        self.repo = EventRepository()

    def get_all(self, db: Session):
        return self.repo.get_all(db)

    def get_by_id(self, db: Session, event_id: int):
        return self.repo.get_by_id(db, event_id)

    def create(self, db: Session, data):
        event = Event(
            **data.dict(), created_at=datetime.now(), updated_at=datetime.now()
        )
        return self.repo.create(db, event)

    def update(self, db: Session, event_id: int, data):
        event = self.repo.get_by_id(db, event_id)
        if not event:
            return None

        event.name = data.name
        event.description = data.description
        event.quota = data.quota
        event.started_at = data.started_at
        event.ended_at = data.ended_at
        event.updated_at = datetime.now()

        return self.repo.update(db, event)

    def delete(self, db: Session, event_id: int):
        event = self.repo.get_by_id(db, event_id)
        if not event:
            return None

        self.repo.delete(db, event)
        return event
