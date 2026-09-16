# preview/__init__.py
"""Пакет предпросмотра интерфейса."""

from .chat_widget import ChatWidget, MessageBubble
from .window import PreviewWindow
from . import style

__all__ = ["ChatWidget", "MessageBubble", "PreviewWindow", "style"]