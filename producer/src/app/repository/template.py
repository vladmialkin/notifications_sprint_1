from app.models.models import NotificationTemplates
from app.repository.base import SQLAlchemyRepository


class NotificationTemplatesRepository(SQLAlchemyRepository[NotificationTemplates]):
    pass


notific_template_repository = NotificationTemplatesRepository(NotificationTemplates)
