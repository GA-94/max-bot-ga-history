# main.py
"""
Точка входа: запускает бота и предпросмотр.
Демо-режим без токена.
"""

import sys

from PyQt5.QtWidgets import QApplication

from bot.config import CHANNEL_NAME
from bot.handlers import handle
from bot.mock_client import MockMaxClient
from preview.window import PreviewWindow


def attach_bot(client: MockMaxClient) -> None:
    """
    Подписка на сообщения пользователя.
    Аналог @bot.router.command("/help") в maxbot_chatbot_python.
    """
    original_send = client.send_from_user

    def wrapped_send(text: str) -> None:
        original_send(text)
        reply = handle(text)
        if reply is None:
            reply = (
                "Команда не распознана.\n"
                "Доступно: /help, /sites, /list"
            )
        client.send_from_bot(reply)

    client.send_from_user = wrapped_send  # type: ignore


def main() -> int:
    app = QApplication(sys.argv)

    client = MockMaxClient(channel_name=CHANNEL_NAME)
    attach_bot(client)

    window = PreviewWindow(client)
    window.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())