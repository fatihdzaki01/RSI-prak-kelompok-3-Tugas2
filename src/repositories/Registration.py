from sqlmodel import Session, select

from src.database.schema.Registration import Registration


class RegistrationRepository:
    def get_all(self, db: Session):
        return db.exec(select(Registration)).all()

    def get_by_id(self, db: Session, registration_id: int):
        return db.get(Registration, registration_id)

    def create(self, db: Session, registration: Registration):
        db.add(registration)
        db.commit()
        db.refresh(registration)
        return registration

    def delete(self, db: Session, registration: Registration):
        db.delete(registration)
        db.commit()

    def get_by_user_and_event(self, db: Session, user_id: int, event_id: int):
        statement = select(Registration).where(
            Registration.user_id == user_id, Registration.event_id == event_id
        )
        return db.exec(statement).first()

    def count_by_event(self, db: Session, event_id: int):
        statement = select(Registration).where(Registration.event_id == event_id)
        return len(db.exec(statement).all())

    def count_by_user(self, db: Session, user_id: int):
        statement = select(Registration).where(Registration.user_id == user_id)
        return len(db.exec(statement).all())
