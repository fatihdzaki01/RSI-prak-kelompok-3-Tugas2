from fastapi import FastAPI
from sqlmodel import SQLModel

from src.database.connection import engine
from src.database.schema import Role
from src.routes.Role import router as role_router

app = FastAPI()


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


create_db_and_table()
app.include_router(role_router)