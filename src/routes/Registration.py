from fastapi import APIRouter

from src.controller.Registration import (
    create_registration,
    delete_registration,
    get_registration,
    get_registrations,
)

router = APIRouter(prefix="/registrations", tags=["registrations"])


router.get("/")(get_registrations)
router.get("/{registration_id}")(get_registration)
router.post("/")(create_registration)
router.delete("/{registration_id}")(delete_registration)
