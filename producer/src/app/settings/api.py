from app.settings.base import Settings


class ApiSettings(Settings):
    TITLE: str = "notification-producer-api"
    OPENAPI_URL: str = "/api/v1/openapi.json"
    DOCS_URL: str = "/api/v1/docs"
    REDOC_URL: str = "/api/v1/redoc"


settings = ApiSettings()
