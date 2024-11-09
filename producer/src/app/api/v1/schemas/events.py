from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class NotificationEvent(BaseModel):
    event_type: str
    notification_channel: list[dict]
    payload: dict
    datetime_to_send: Optional[datetime]


class DeferredNotifications(BaseModel):
    notification_list: list
