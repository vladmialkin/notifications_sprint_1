from app.settings.base import Settings


class JwtSettings(Settings):
    AUTH_API_URL: str
    JWT_ALGORITHM: str
    AUDIENCE: str
    SECRET_KEY: str


settings = JwtSettings()
