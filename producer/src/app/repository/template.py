from app.models.models import NotificationTemplates
from app.repository.base import SQLAlchemyRepository


class NotificationTemplatesRepository(SQLAlchemyRepository[NotificationTemplates]):
    pass


template_repository = NotificationTemplatesRepository(NotificationTemplates)
