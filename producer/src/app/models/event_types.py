from enum import Enum
from pydantic import BaseModel, Field


class Topics(Enum):
    REGISTRATION = "registration"
    USER_LOGIN = "user_login"
    NEW_EPISODE = "new_episode"
    NEW_LIKE = "new_like"
    SUBSCRIPTION_DISCOUNT = "subscription_discount"


class UserLogin(BaseModel):
    user_id: str = Field(title="UUID", description="Идентификатор пользователя")
    user_name: str = Field(title="User name", description="Имя пользователя")
    user_agent: str = Field(title="User agent")


class Registration(BaseModel):
    user_id: str = Field(title="UUID", description="Идентификатор пользователя")
    user_name: str = Field(title="User name", description="Имя пользователя")


class NewEpisode(BaseModel):
    pass


class NewLike(BaseModel):
    pass


class SubscriptionDiscount(BaseModel):
    pass


class Notification(BaseModel):
    id: str = Field(title="UUID", description="Идентификатор уведомления")
    user_id: str = Field(title="UUID", description="Идентификатор пользователя")
    type_id: str = Field(title="UUID", description="Идентификатор типа уведомления")
    content_id: str = Field(title="UUID", description="Идентификатор данных уведомления")
    template_id: str = Field(title="UUID", description="Идентификатор шаблона уведомления")
    status_id: str = Field(title="UUID", description="Идентификатор статуса уведомления")
