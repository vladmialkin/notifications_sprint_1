import asyncio

import aiohttp
from app.db.postgres import connect_to_db


async def fetch_notifications(conn):
    result = await conn.fetch(
        """SELECT * FROM notifications 
        WHERE datetime_to_send 
        BETWEEN NOW() AND NOW() + INTERVAL '10 minutes';"""
    )
    return result


async def send_notifications(notifications):
    notification_url = "http://notification_producer:8090/api/v1/notifications/deferred_notification"

    async with aiohttp.ClientSession() as session:
        for notification in notifications:
            async with session.post(notification_url, json=dict(notification)) as response:
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
