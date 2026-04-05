from fastapi import APIRouter
from src.controller import account

from src.controller.Account import (
    create_account,
    delete_account,
    get_account,
    get_accounts,
    update_account
)
from src.dto.Account import AccountResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])


router.get("/")(account.get_accounts)
router.get("/{account_id}")(account.get_account)
router.post("/")(account.create_account)
router.put("/{account_id}")(account.update_account)
router.delete("/{account_id}")(account.delete_account)