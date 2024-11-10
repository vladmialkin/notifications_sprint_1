import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.models.constance import TypeEnum, StatusEnum, ChannelEnum
from app.models.models import NotificationTypes, NotificationStatus, Channels
from app.settings.postgresql import settings as pg_settings
from app.repository.notification_type import notific_type_repository
from app.repository.notification_status import status_repository
from app.repository.channel import channel_repository


engine = create_async_engine(pg_settings.DSN, echo=pg_settings.LOG_QUERIES)
session = async_sessionmaker(engine, expire_on_commit=False)


async def fill_notification_type_table():
    async with session() as s:
        for type_ in TypeEnum:
            data = NotificationTypes(
                name=type_.value,
                is_instant=True if type_.value in ['registration', 'user_login', 'new_episode'] else False
            )
            await notific_type_repository.create(session=s, data=data.to_dict())


async def fill_notification_status_table():
    async with session() as s:
        for status in StatusEnum:
            data = NotificationStatus(status=status.value)
            await status_repository.create(session=s, data=data.to_dict())


async def fill_channel_table():
    async with session() as s:
        for channel in ChannelEnum:
            data = Channels(channel=channel.value)
            await channel_repository.create(session=s, data=data.to_dict())


if __name__ == "__main__":
    asyncio.run(fill_notification_type_table())
    asyncio.run(fill_notification_status_table())
    asyncio.run(fill_channel_table())
