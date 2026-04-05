from fastapi import APIRouter
from src.controller import account

router = APIRouter(prefix="/accounts", tags=["Accounts"])


router.get("/")(account.get_accounts)
router.get("/{account_id}")(account.get_account)
router.post("/")(account.create_account)
router.put("/{account_id}")(account.update_account)
router.delete("/{account_id}")(account.delete_account)