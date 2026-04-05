from fastapi import FastAPI
from sqlmodel import SQLModel

from src.database.connection import engine
from src.database.schema import Event, Registration, User
from src.routes.Event import router as event_router
from src.routes.Registration import router as registration_router
from src.routes.User import router as user_router

app = FastAPI(title="Event Registration API")


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_table()


app.include_router(user_router)
app.include_router(event_router)
app.include_router(registration_router)
