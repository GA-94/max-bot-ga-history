# bot/__init__.py
"""Пакет бота «История Алтая БОТ»."""

from .config import BOT_NAME, CHANNEL_NAME
from .handlers import handle, is_command
from .mock_client import MockMaxClient, Message

__all__ = [
    "BOT_NAME",
    "CHANNEL_NAME",
    "handle",
    "is_command",
    "MockMaxClient",
    "Message",
]