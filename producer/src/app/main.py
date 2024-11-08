import json
from contextlib import asynccontextmanager

from aiokafka import AIOKafkaProducer
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.api.deps.kafka import kafka_producer
from app.db import postgresql
from app.api.v1.router import router
from app.settings.api import settings as api_settings
from app.settings.kafka import settings as kafka_settings
from app.settings.postgresql import settings as postgresql_settings


def serializer(value):
    return json.dumps(value).encode()


@asynccontextmanager
async def lifespan(_: FastAPI):
    kafka_producer = AIOKafkaProducer(
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
    await kafka_producer.start()
    yield
    await kafka_producer.stop()
    await postgresql.async_engine.dispose()


app = FastAPI(
    title=api_settings.TITLE,
    openapi_url=api_settings.OPENAPI_URL,
    docs_url=api_settings.DOCS_URL,
    redoc_url=api_settings.REDOC_URL,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

origins = [
    "http://localhost:8070"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
