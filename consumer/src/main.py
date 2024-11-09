import asyncio
from contextlib import closing

from aiokafka import AIOKafkaConsumer
from aiosmtplib import SMTP

from services.builder.html import FromHTMLTemplateBuilder
from services.consumer.kafka import KafkaConsumer
from services.consumer.utils import kafka_aclosing
from services.sender.smtp import EmailSender
from settings.kafka import settings as kafka_settings
from settings.smtp import settings as smtp_settings


async def run_notification_process(
    kafka_conn: AIOKafkaConsumer, smpt_conn: SMTP
) -> None:
    consumer = KafkaConsumer(kafka_conn)
    sender = EmailSender(smpt_conn)
    builder = FromHTMLTemplateBuilder()

    async for notification in consumer.consume():
        tasks = [sender.send(email) for email in builder.build(notification)]
        await asyncio.gather(*tasks)


async def main() -> None:
    kafka_consumer_client = AIOKafkaConsumer(
        kafka_settings.KAFKA_TOPICS,
        bootstrap_servers=kafka_settings.KAFKA_BOOTSTRAP_SERVERS,
        enable_auto_commit=True,
    )

    smtp_client = SMTP(
        smtp_settings.SMTP_HOST,
        smtp_settings.SMTP_PORT,
        smtp_settings.SMTP_USER,
        smtp_settings.SMTP_PASSWORD.get_secret_value(),
    )

    async with kafka_aclosing(kafka_consumer_client), closing(smtp_client):
        await run_notification_process(kafka_consumer_client, smtp_client)


if __name__ == "__main__":
    asyncio.run(main())
