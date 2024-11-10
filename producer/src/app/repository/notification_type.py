from app.models.models import NotificationTypes
from app.repository.base import SQLAlchemyRepository


class NotificationTypeRepository(SQLAlchemyRepository[NotificationTypes]):
    pass


notific_type_repository = NotificationTypeRepository(NotificationTypes)
