from app.models.models import Channels
from app.repository.base import SQLAlchemyRepository


class ChannelRepository(SQLAlchemyRepository[Channels]):
    pass


channel_repository = ChannelRepository(Channels)
