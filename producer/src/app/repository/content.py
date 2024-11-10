from app.models.models import Contents
from app.repository.base import SQLAlchemyRepository


class ContentRepository(SQLAlchemyRepository[Contents]):
    pass


content_repository = ContentRepository(Contents)
