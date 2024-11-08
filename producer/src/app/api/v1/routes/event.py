from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import DBAPIError

# from app.api.deps.kafka import Producer
from app.api.deps.session import Session
from app.api.deps.user import UserData
from app.api.v1.schemas.events import Event
from app.repository.notification_type import notific_type_repository
from app.repository.content import content_repository
from app.models.event_types import get_topic_by_event
from app.models.message import KafkaPayload

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def send_message(
    event: Event,
    session: Session,
    # producer: Producer,
    user: UserData,
) -> None:
    """Ендпоинт для создания уведомления исходя из типа уведомления."""

    print(f'\nHARRY POTTER\n')
    print(event)
    print(user)

    try:
        type_obj = await notific_type_repository.get(session, name=event.event_type)
        type_id, is_instant = type_obj.id, type_obj.is_instant
    except DBAPIError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    content_obj = await content_repository.create(session, data=event.payload)


    # topic = await get_topic_by_event(msg.event_type)
    #
    # if topic is None:
    #     raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #
    # payload = KafkaPayload(
    #     topic=topic, key=msg.user_id, value=msg.model_dump_json()
    # )
    #
    # try:
    #     await producer.send(**payload.model_dump())
    # except TypeError as e:
    #     raise HTTPException(
    #         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.args
    #     )
