from app.models.models import NotificationStatus
from app.repository.base import SQLAlchemyRepository


class NotificationStatusRepository(SQLAlchemyRepository[NotificationStatus]):
    pass


status_repository = NotificationStatusRepository(NotificationStatus)
