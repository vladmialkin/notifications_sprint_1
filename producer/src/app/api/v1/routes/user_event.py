from fastapi import APIRouter, HTTPException, status

from src.app import Producer
from src.app import UserData
from src.app import (
    ChangeVideoQuality,
    Click,
    PageView,
    TimeOnPage,
    UsingSearchFilters,
    WatchToTheEnd,
)
from src.app import get_topic_by_event
from src.app import KafkaPayload

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def send_message(
    msg: Click
    | PageView
    | TimeOnPage
    | ChangeVideoQuality
    | WatchToTheEnd
    | UsingSearchFilters,
    producer: Producer,
    user: UserData,
) -> None:
    """Ендпоинт для обработки события исходя из типа этого события и отправки сообщения в Kafka."""
    topic = await get_topic_by_event(msg.event_type)

    if topic is None:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    payload = KafkaPayload(
        topic=topic, key=msg.user_id, value=msg.model_dump_json()
    )

    try:
        await producer.send(**payload.model_dump())
    except TypeError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.args
        )
