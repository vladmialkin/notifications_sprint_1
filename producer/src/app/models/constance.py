from enum import Enum


NAME_STR_LEN = 128
EMAIL_STR_LEN = 128
PASSWORD_STR_LEN = 128
CHANNEL = 32
STATUS = 32
NOTIFICATION_TYPE = 256
DESCRIPTION = 512


class ChannelEnum(str, Enum):
    EMAIL = 'email'
    SMS = 'sms'
    WEBSOCKET = 'websocket'


class StatusEnum(str, Enum):
    PENDING = 'pending'
    SENT = 'sent'
    FAILED = 'failed'


class TypeEnum(str, Enum):
    REGISTRATION = 'registration'
    USER_LOGIN = 'user_login'
    NEW_EPISODE = 'new_episode'
    NEW_LIKE = 'new_like'
    SUBSCRIPTION_DISCOUNT = 'subscription_discount'
