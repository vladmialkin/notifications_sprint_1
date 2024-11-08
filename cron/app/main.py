import asyncio

from app.db.postgres import connect_to_db


async def check_messages(conn):
    pass


async def main():
    connection = await connect_to_db()


if __name__ == '__main__':
    asyncio.run(main())
