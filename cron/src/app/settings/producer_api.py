from app.settings.base import Settings


class ProducerApiSettings(Settings):
    PRODUCER_URL: str


settings = ProducerApiSettings()
