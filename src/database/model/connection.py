from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql://postgres-rsi:4321@localhost:5435/rsiprak_kelompok3_tugas2"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session