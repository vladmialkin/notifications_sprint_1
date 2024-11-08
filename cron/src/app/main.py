import asyncio

from src.app.db.postgres import connect_to_db


async def check_messages(conn):
    result = await conn.execute(
        """SELECT * FROM notifications 
        WHERE datetime_to_send 
        BETWEEN NOW() AND NOW() + INTERVAL '10 minutes';"""
    )
    print(result)


async def main():
    connection = await connect_to_db()
    await check_messages(connection)


if __name__ == '__main__':
    asyncio.run(main())
