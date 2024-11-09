from typing import AsyncGenerator
from aiokafka import AIOKafkaConsumer, ConsumerRecord
from schemas.notification import Notification


class KafkaConsumer:
    def __init__(self, conn: AIOKafkaConsumer) -> None:
        self._conn = conn

    async def consume(self) -> AsyncGenerator[ConsumerRecord, None]:
        async for msg in self._conn:
            try:
                yield Notification(**msg.value)
            except Exception as e:
                print(e)
