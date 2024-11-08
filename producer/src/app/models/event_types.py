from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    user_id: str = Field(title="UUID", description="Идентификатор пользователя")
    user_name: str = Field(title="User name", description="Имя пользователя")
    user_agent: str = Field(title="User agent")


class Register(BaseModel):
    pass
