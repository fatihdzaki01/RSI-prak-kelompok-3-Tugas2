from sqlmodel import Session

from src.database.schema.Event import Event
from src.database.schema.Registration import Registration
from src.repositories.Registration import RegistrationRepository


class RegistrationService:
    def __init__(self):
        self.repo = RegistrationRepository()

    def create(self, db: Session, user_id: int, event_id: int):
        # cek event ada atau tidak
        event = db.get(Event, event_id)
        if not event:
            raise ValueError("event tidak ditemukan")

        # buat ngecek apakah user udah daftar apa blm
        existing = self.repo.get_by_user_and_event(db, user_id, event_id)
        if existing:
            raise ValueError("user sudah terdaftar di event ini")

        # buat ngecek kuota
        total = self.repo.count_by_event(db, event_id)
        if total >= event.quota:
            raise ValueError("maaf, kuota event ini udah penuh")

        # untuk registrasi/ create
        registration = Registration(user_id=user_id, event_id=event_id)

        return self.repo.create(db, registration)

    def delete(self, db: Session, registration_id: int):
        registration = self.repo.get_by_id(db, registration_id)
        if not registration:
            raise ValueError("registrasi tidak ditemukan!")

        self.repo.delete(db, registration)
        return {"message": "Berhasil dibatalkan"}

    def get_all(self, db: Session):
        return self.repo.get_all(db)

    def get_by_id(self, db: Session, registration_id: int):
        return self.repo.get_by_id(db, registration_id)
