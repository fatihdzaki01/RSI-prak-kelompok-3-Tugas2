from fastapi import Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.dto.Registration import RegistrationCreate
from src.services.Registration import RegistrationService

service = RegistrationService()


def get_registrations(db: Session = Depends(get_session)):
    return service.get_all(db)


def get_registration(registration_id: int, db: Session = Depends(get_session)):
    return service.get_by_id(db, registration_id)


def create_registration(data: RegistrationCreate, db: Session = Depends(get_session)):
    return service.create(db, data.user_id, data.event_id)


def delete_registration(registration_id: int, db: Session = Depends(get_session)):
    return service.delete(db, registration_id)