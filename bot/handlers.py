# bot/handlers.py
"""
Обработчики команд.
Не знают ни про PyQt5, ни про MAX — только текст.
"""

from .config import HELP_TEXT, LIST_TEXT, SITES_TEXT


def handle(text: str) -> str | None:
    """Возвращает ответ или None, если команда неизвестна."""
    cmd = (text or "").strip().lower()

    if cmd == "/help":
        return HELP_TEXT
    if cmd == "/sites":
        return SITES_TEXT
    if cmd == "/list":
        return LIST_TEXT

    # словесные синонимы
    if cmd in ("help", "помощь"):
        return HELP_TEXT
    if cmd in ("sites", "сайты", "ссылки"):
        return SITES_TEXT
    if cmd in ("list", "список", "меню"):
        return LIST_TEXT

    return None


def is_command(text: str) -> bool:
    """Начинается ли текст со слэша."""
    return (text or "").strip().startswith("/")