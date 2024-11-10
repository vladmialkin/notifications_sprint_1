from pydantic import BaseModel, Field


class Notification(BaseModel):
    id: str = Field(title="UUID", description="Идентификатор уведомления")
    user_id: str = Field(title="UUID", description="Идентификатор пользователя")
    type_id: str = Field(title="UUID", description="Идентификатор типа уведомления")
    content_id: str = Field(title="UUID", description="Идентификатор данных уведомления")
    template_id: str = Field(title="UUID", description="Идентификатор шаблона уведомления")
    status_id: str = Field(title="UUID", description="Идентификатор статуса уведомления")


class DeferredNotifications(BaseModel):
    notification_payload: Notification
