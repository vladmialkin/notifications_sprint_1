from schemas.base import Base
from pydantic import EmailStr


class Email(Base):
    sender: EmailStr
    recipients: list[EmailStr]
    message: str
