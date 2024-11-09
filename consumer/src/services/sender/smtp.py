from aiosmtplib import SMTP

from schemas.email import Email
from settings.smtp import settings as smtp_settings


class EmailSender:
    def __init__(self, conn: SMTP) -> None:
        self._conn = conn

    async def send(self, email: Email) -> None:
        await self._conn.sendmail(
            smtp_settings.SMTP_USER, email.recipient, email.message
        )
