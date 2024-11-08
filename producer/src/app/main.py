import json
from contextlib import asynccontextmanager

from aiokafka import AIOKafkaProducer
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.app import kafka
from src.app import postgresql
from src.app import router
from src.app.settings import settings as api_settings
from src.app.settings import settings as kafka_settings
from src.app.settings import settings as postgresql_settings


def serializer(value):
    return json.dumps(value).encode()


@asynccontextmanager
async def lifespan(_: FastAPI):
    kafka.kafka_producer = AIOKafkaProducer(
        client_id="ugc_producer",
        bootstrap_servers=f"{kafka_settings.KAFKA_HOST}:{kafka_settings.KAFKA_PORT}",
        value_serializer=serializer,
        key_serializer=serializer,
        compression_type="gzip",
    )
    postgresql.async_engine = create_async_engine(
        postgresql_settings.DSN,
        echo=postgresql_settings.LOG_QUERIES,
    )
    postgresql.async_session = async_sessionmaker(
        postgresql.async_engine, expire_on_commit=False
    )
    await kafka.kafka_producer.start()
    yield
    await kafka.kafka_producer.stop()
    await postgresql.async_engine.dispose()


app = FastAPI(
    title=api_settings.TITLE,
    openapi_url=api_settings.OPENAPI_URL,
    docs_url=api_settings.DOCS_URL,
    redoc_url=api_settings.REDOC_URL,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(router)
