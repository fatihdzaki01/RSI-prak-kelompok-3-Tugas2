from fastapi import APIRouter
from src.controllers import users

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
def get_events():
    return users.get_events()

@router.get("/{user_id}")
def get_event(user_id: int):
    return users.get_event(user_id)

@router.post("/")
def create_event():
    return users.create_event()

@router.put("/{user_id}")
def update_event(user_id: int):
    return users.update_event(user_id)

@router.delete("/{user_id}")
def delete_event(user_id: int):
    return users.delete_event(user_id)