from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "postgresql://postgres-rsi:4321@localhost:5435/rsi_db_tugas2"

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
