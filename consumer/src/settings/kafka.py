from settings.base import Settings


class KafkaSettings(Settings):
    KAFKA_TOPICS: list[str]
    KAFKA_BOOTSTRAP_SERVERS: list[str]


settings = KafkaSettings()
