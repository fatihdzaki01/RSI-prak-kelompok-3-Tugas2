from fastapi import Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.dto.Event import EventCreate
from src.services.Event import EventService

service = EventService()


def get_events(db: Session = Depends(get_session)):
    return service.get_all(db)


def get_event(event_id: int, db: Session = Depends(get_session)):
    return service.get_by_id(db, event_id)


def create_event(data: EventCreate, db: Session = Depends(get_session)):
    return service.create(db, data)


def update_event(event_id: int, data: EventCreate, db: Session = Depends(get_session)):
    return service.update(db, event_id, data)


def delete_event(event_id: int, db: Session = Depends(get_session)):
    return service.delete(db, event_id)
