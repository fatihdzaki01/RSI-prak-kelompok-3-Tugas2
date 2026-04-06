from fastapi import APIRouter

from src.controller.Account import (
    create_account,
    delete_account,
    get_account,
    get_accounts,
    update_account,
)

router = APIRouter(prefix="/accounts", tags=["Accounts"])


router.get("/")(get_accounts)
router.get("/{account_id}")(get_account)
router.post("/")(create_account)
router.put("/{account_id}")(update_account)
router.delete("/{account_id}")(delete_account)
