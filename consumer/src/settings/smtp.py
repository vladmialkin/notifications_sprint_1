from settings.base import Settings
from pydantic import SecretStr


class SMTPSettings(Settings):
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 25
    SMTP_USER: str
    SMTP_PASSWORD: SecretStr


settings = SMTPSettings()
