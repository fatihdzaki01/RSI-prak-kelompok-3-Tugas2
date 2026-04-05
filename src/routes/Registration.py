from fastapi import APIRouter

from src.controller.Registration import (
    create_registration,
    delete_registration,
    get_registration,
    get_registrations,
)
from src.dto.Registration import RegistrationResponse

router = APIRouter(prefix="/registrations", tags=["Registrations"])


router.get("", response_model=list[RegistrationResponse])(get_registrations)
router.get("/{registration_id}", response_model=RegistrationResponse)(get_registration)
router.post("", response_model=RegistrationResponse)(create_registration)
router.delete("/{registration_id}", status_code=204)(delete_registration)