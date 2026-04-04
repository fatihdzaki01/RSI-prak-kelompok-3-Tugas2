from fastapi import FastAPI
from sqlmodel import SQLModel

from src.database.model.connection import engine
from src.database.model import models
from src.routes.users import router as users_router


app = FastAPI()


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


create_db_and_table()
app.include_router(users_router)