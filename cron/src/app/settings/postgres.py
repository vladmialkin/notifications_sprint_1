from src.app.settings.base import Settings


class PostgreSQLSettings(Settings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str


settings = PostgreSQLSettings()
