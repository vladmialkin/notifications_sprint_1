from settings.base import Settings


class LoggingSettings(Settings):
    LOG_FILE_PATH: str = "/var/log/.log"
    LOG_FORMAT: str = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    LOG_NAME: str = "email_notification_consumer"


settings = LoggingSettings()
