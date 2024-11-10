from app.models.models import NotificationChannel
from app.repository.base import SQLAlchemyRepository


class NotificationChannelRepository(SQLAlchemyRepository[NotificationChannel]):
    pass


notific_channel_repository = NotificationChannelRepository(NotificationChannel)
