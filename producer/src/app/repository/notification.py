from app.models.models import Notifications
from app.repository.base import SQLAlchemyRepository


class NotificationRepository(SQLAlchemyRepository[Notifications]):
    pass


notification_repository = NotificationRepository(Notifications)
