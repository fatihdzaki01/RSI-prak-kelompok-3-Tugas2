from fastapi import FastAPI
from src.routes import account

app = FastAPI()

app.include_router(account.router)