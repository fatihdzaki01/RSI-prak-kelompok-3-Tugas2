from fastapi import FastAPI
from sqlmodel import SQLModel

from src.database.connection import engine
from src.database.schema import Event, Registration
from src.routes.Event import router as event_router
from src.routes.Registration import router as registration_router

app = FastAPI()


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


create_db_and_table()
app.include_router(event_router)
app.include_router(registration_router)
