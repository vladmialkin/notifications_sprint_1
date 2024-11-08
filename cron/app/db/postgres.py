from asyncpg import connect
import backoff
from app.settings.logging import logger
from app.settings.postgres import settings as postgres_settings


@backoff.on_exception(backoff.expo, Exception, max_tries=5)
async def connect_to_db():
    logger.info("Попытка подключения к базе данных...")
    conn = await connect(
        user=postgres_settings.POSTGRES_USER,
        password=postgres_settings.POSTGRES_PASSWORD,
        database=postgres_settings.POSTGRES_DB,
        host=postgres_settings.POSTGRES_HOST,
        port=postgres_settings.POSTGRES_PORT,
    )
    logger.info("Подключение к базе данных установлено.")
    return conn
