from aiosmtplib import SMTP


class EmailSender:
    def __init__(self, conn: SMTP) -> None:
        self._conn = conn

    async def send(self, sender: str, recipients: list[str], message: str) -> None:
        await self._conn.sendmail(sender, recipients, message)
