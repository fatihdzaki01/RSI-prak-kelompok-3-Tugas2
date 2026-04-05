from fastapi import APIRouter

from src.controller.Event import (
    create_event,
    delete_event,
    get_event,
    get_events,
    update_event,
)

router = APIRouter(prefix="/events", tags=["Events"])


router.get("/")(get_events)
router.get("/{event_id}")(get_event)
router.post("/")(create_event)
router.put("/{event_id}")(update_event)
router.delete("/{event_id}")(delete_event)