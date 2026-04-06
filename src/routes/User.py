from fastapi import APIRouter

from src.controller.User import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
)
from src.dto.User import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


router.get("/", response_model=list[UserResponse])(get_users)
router.get("/{user_id}", response_model=UserResponse)(get_user)
router.post("/", response_model=UserResponse)(create_user)
router.put("/{user_id}", response_model=UserResponse)(update_user)
router.delete("/{user_id}")(delete_user)