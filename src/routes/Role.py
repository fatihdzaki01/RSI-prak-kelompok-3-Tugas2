from fastapi import APIRouter

from src.controller.Role import (
    create_role,
    delete_role,
    get_role,
    get_roles,
    update_role,
)

router = APIRouter(prefix="/roles", tags=["Roles"])


router.get("/")(get_roles)
router.get("/{role_id}")(get_role)
router.post("/")(create_role)
router.put("/{role_id}")(update_role)
router.delete("/{role_id}")(delete_role)
