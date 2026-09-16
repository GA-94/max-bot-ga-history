# bot/mock_client.py
"""
Мок-клиент MAX. Эмуляция без токена и без сети.
Паттерн «издатель — подписчик».
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable, List


@dataclass
class Message:
    author: str  # "bot" | "user" | "system"
    text: str
    time: datetime = field(default_factory=datetime.now)


class MockMaxClient:
    """Синтетический клиент MAX."""

    def __init__(self, channel_name: str):
        self.channel_name = channel_name
        self.messages: List[Message] = []
        self._subscribers: List[Callable[[], None]] = []

        self._add_system(f"Канал «{channel_name}» создан")
        self._add_system("Готов к работе. Команды: /help, /sites, /list")

    # ---------- подписка ----------
    def subscribe(self, callback: Callable[[], None]) -> None:
        self._subscribers.append(callback)

    def _notify(self) -> None:
        for cb in self._subscribers:
            cb()

    # ---------- внутреннее ----------
    def _add(self, msg: Message) -> None:
        self.messages.append(msg)
        self._notify()

    def _add_system(self, text: str) -> None:
        self._add(Message(author="system", text=text))

    # ---------- публичный API ----------
    def send_from_user(self, text: str) -> None:
        self._add(Message(author="user", text=text))

    def send_from_bot(self, text: str) -> None:
        self._add(Message(author="bot", text=text))

    def clear(self) -> None:
        self.messages.clear()
        self._notify()