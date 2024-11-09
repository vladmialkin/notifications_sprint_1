from uuid import UUID
from schemas.base import Base


class Notification(Base):
    id: UUID
    users: dict
    template: ...
