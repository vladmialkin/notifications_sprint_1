from datetime import datetime
from uuid import UUID as PY_UUID

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    String,
    Table,
    Boolean,
    Enum, JSON, Text, text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, mapper_registry
from app.models.constance import (
    DESCRIPTION,
    ChannelEnum,
    StatusEnum,
    TypeEnum
)


notification_channel = Table(
    "notificationchannel",
    Base.metadata,
    Column("id", UUID, primary_key=True, server_default=text("gen_random_uuid()")),
    Column("notification_id", ForeignKey("notifications.id"), primary_key=True),
    Column("channel_id", ForeignKey("channels.id"), primary_key=True),
)


class NotificationChannel:
    pass


mapper_registry.map_imperatively(NotificationChannel, notification_channel)


class Channels(Base):
    channel: Mapped[str] = mapped_column(Enum(ChannelEnum), nullable=False, unique=True)
    notifications = relationship("Notifications", secondary=notification_channel, back_populates="channels")


class NotificationTypes(Base):
    name: Mapped[str] = mapped_column(Enum(TypeEnum), nullable=False, unique=True)
    is_instant: Mapped[bool] = mapped_column(Boolean, nullable=False)
    description: Mapped[str] = mapped_column(String(DESCRIPTION), nullable=True)

    contents: Mapped[list["Contents"]] = relationship("Contents", back_populates="notification_types")
    notifications: Mapped[list["Notifications"]] = relationship("Notifications", back_populates="notification_types")
    templates: Mapped[list["NotificationTemplates"]] = relationship("NotificationTemplates", back_populates="types")


class NotificationTemplates(Base):
    type_id: Mapped[PY_UUID] = mapped_column(ForeignKey('notificationtypes.id'), unique=True)
    template: Mapped[str] = mapped_column(Text, nullable=False, unique=True)

    notifications: Mapped[list["Notifications"]] = relationship("Notifications", back_populates="templates")
    types: Mapped[NotificationTypes] = relationship("NotificationTypes", back_populates="templates")


class NotificationStatus(Base):
    status: Mapped[str] = mapped_column(Enum(StatusEnum), nullable=False, unique=True)

    notifications: Mapped[list["Notifications"]] = relationship("Notifications", back_populates="notification_status")


class Notifications(Base):
    user_id: Mapped[PY_UUID] = mapped_column(UUID, nullable=False)
    type_id: Mapped[PY_UUID] = mapped_column(ForeignKey('notificationtypes.id'))
    content_id: Mapped[PY_UUID] = mapped_column(ForeignKey('contents.id'), unique=True)
    template_id: Mapped[PY_UUID] = mapped_column(ForeignKey('notificationtemplates.id'))
    status_id: Mapped[PY_UUID] = mapped_column(ForeignKey('notificationstatus.id'))
    datetime_to_send: Mapped[datetime] = mapped_column(DateTime(timezone=False))

    notification_types: Mapped[NotificationTypes] = relationship("NotificationTypes", back_populates="notifications")
    notification_status: Mapped[NotificationStatus] = relationship("NotificationStatus", back_populates="notifications")
    templates: Mapped[NotificationTemplates] = relationship("NotificationTemplates", back_populates="notifications")
    content: Mapped["Contents"] = relationship("Contents", back_populates="notification")
    channels: Mapped[list["Channels"]] = relationship("Channels", secondary=notification_channel, back_populates="notifications")


class Contents(Base):
    type_id: Mapped[PY_UUID] = mapped_column(ForeignKey('notificationtypes.id'))
    payload: Mapped[str] = mapped_column(JSON, nullable=False)

    notification_types: Mapped[NotificationTypes] = relationship("NotificationTypes", back_populates="contents")
    notification: Mapped["Notifications"] = relationship("Notifications", back_populates="content", uselist=False)
