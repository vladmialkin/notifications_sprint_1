import asyncio

import aiohttp
from app.db.postgres import connect_to_db
from app.settings.producer_api import settings as producer_api_settings


async def fetch_notifications(conn):
    result = await conn.fetch(
        """SELECT * FROM notifications 
        WHERE datetime_to_send 
        BETWEEN NOW() AND NOW() + INTERVAL '10 minutes';"""
    )
    return result


async def send_notifications(notifications):
    async with aiohttp.ClientSession() as session:
        for notification in notifications:
            async with session.post(producer_api_settings.PRODUCER_URL, json=dict(notification)) as response:
                if response.status == 200:
                    print("Уведомление успешно отправлено:", await response.json())
                else:
                    print("Ошибка отправки уведомления:", response.status, await response.text())


async def main():
    connection = await connect_to_db()
    notifications =await fetch_notifications(connection)
    await send_notifications(notifications)


if __name__ == '__main__':
    asyncio.run(main())
