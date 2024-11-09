import datetime
import pprint

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import DBAPIError

from app.api.deps.kafka import Producer
from app.api.deps.user_agent import UserAgent
from app.api.deps.session import Session
from app.api.deps.user import UserData
from app.api.v1.schemas.events import NotificationEvent, DeferredNotifications
from app.repository.notification_type import notific_type_repository
from app.repository.content import content_repository
from app.repository.template import template_repository
from app.repository.notification_status import status_repository
from app.repository.channel import channel_repository
from app.repository.notification import notification_repository
from app.repository.notification_channel import notific_channel_repository
from app.models.event_types import UserLogin, Topics
from app.models.constance import StatusEnum
from app.models.message import KafkaPayload
from app.models.models import Notifications, Contents

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def send_message(
    event: NotificationEvent,
    session: Session,
    producer: Producer,
    user: UserData,
    user_agent: UserAgent
) -> None:
    """Ендпоинт для создания уведомления исходя из типа уведомления."""

    print(f'\nNotificationEvent:')
    pprint.pprint(event.model_dump())

    # 1, 2, 3
    try:
        type_obj = await notific_type_repository.get(session, name=event.event_type)
        status_obj = await status_repository.get(session, status=StatusEnum.CREATED.value)

        if any([type_obj, status_obj]) is None:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

        template_obj = await template_repository.get(session, type_id=type_obj.id)
        if template_obj is None:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except DBAPIError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # 4
    content_data = Contents(
        type_id=type_obj.id,
        payload=UserLogin(
            user_id=str(user.id),
            user_name=event.payload.get('user_name'),
            user_agent=user_agent
        ).model_dump()
    )
    content_obj = await content_repository.create(session, data=content_data.to_dict())

    # 5
    notific_data = Notifications(
        type_id=type_obj.id,
        content_id=content_obj.id,
        template_id=template_obj.id,
        user_id=user.id,
        status_id=status_obj.id,
        datetime_to_send=datetime.datetime.now()
    )
    notification_obj = await notification_repository.create(session, data=notific_data.to_dict())

    # 6, 7
    for channel_dict in event.notification_channel:
        channel_obj = await channel_repository.get(session, channel=channel_dict.get('channel'))

        channel_data = {
            'channel_id': channel_obj.id,
            'notification_id': notification_obj.id,
            'value': channel_dict.get('value')
        }
        await notific_channel_repository.create(session, data=channel_data)

    # Send to Kafka
    topic = Topics.INSTANT.value if type_obj.is_instant else Topics.DEFERRED.value

    payload = KafkaPayload(
        topic=topic, key=user.id, value=notification_obj.id
    )

    try:
        await producer.send(**payload.model_dump())
    except TypeError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.args
        )


@router.post("/deferred_notification", status_code=status.HTTP_200_OK)
async def send_deferred_notification(
    event: DeferredNotifications,
    session: Session,
    producer: Producer,
    user: UserData,
    user_agent: UserAgent
) -> None:
    print(1)
    print(event)
