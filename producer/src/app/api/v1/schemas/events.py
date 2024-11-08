from pydantic import BaseModel, Field

from app.models.event_types import EventTypes


class NotifyEvent(BaseModel):
    type: str
    payload: str
