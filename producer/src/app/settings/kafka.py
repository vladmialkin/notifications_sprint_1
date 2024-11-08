from src.app import Settings


class KafkaSettings(Settings):
    KAFKA_HOST: str
    KAFKA_PORT: int


settings = KafkaSettings()
