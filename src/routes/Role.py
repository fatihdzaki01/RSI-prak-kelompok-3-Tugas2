from fastapi import APIRouter
from src.controller import Role

router = APIRouter(prefix="/roles", tags=["Roles"])


router.get("/")(Role.get_roles)
router.get("/{role_id}")(Role.get_role)
router.post("/")(Role.create_role)
router.put("/{role_id}")(Role.update_role)
router.delete("/{role_id}")(Role.delete_role)