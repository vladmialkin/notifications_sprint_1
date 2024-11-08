from fastapi import APIRouter, HTTPException, status

from app.api.deps.kafka import Producer
from app.api.deps.user import UserData
from app.api.v1.schemas.events import NotifyEvent

from app.models.event_types import get_topic_by_event
from app.models.message import KafkaPayload

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def send_message(
    msg: NotifyEvent,
    producer: Producer,
    # user: UserData,
) -> None:
    pass
