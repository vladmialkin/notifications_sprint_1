from pydantic import BaseModel, Field
from typing import Any


class DeferredNotifications(BaseModel):
    notification_list: Any


class Notification(BaseModel):
    id: str = Field(title="UUID", description="Идентификатор уведомления")
    user_id: str = Field(title="UUID", description="Идентификатор пользователя")
    type_id: str = Field(title="UUID", description="Идентификатор типа уведомления")
    content_id: str = Field(title="UUID", description="Идентификатор данных уведомления")
    template_id: str = Field(title="UUID", description="Идентификатор шаблона уведомления")
    status_id: str = Field(title="UUID", description="Идентификатор статуса уведомления")
