# preview/window.py
"""
Главное окно предпросмотра: боковая панель и чат.
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QFrame,
)

from bot.mock_client import MockMaxClient
from preview.chat_widget import ChatWidget
from . import style


class PreviewWindow(QMainWindow):
    """Окно предпросмотра (демо-режим MAX)."""

    def __init__(self, client: MockMaxClient):
        super().__init__()
        self.client = client

        self.setWindowTitle(f"MAX — {client.channel_name}")
        self.resize(1120, 740)

        central = QWidget()
        central.setStyleSheet(f"background: {style.BG_APP};")
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ------------------------------------------------
        #  Левая панель
        # ------------------------------------------------
        sidebar = QFrame()
        sidebar.setFixedWidth(260)
        sidebar.setStyleSheet(
            f"QFrame {{"
            f"  background: {style.BG_SIDEBAR};"
            f"  border-right: 1px solid {style.BORDER};"
            f"}}"
        )

        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(20, 20, 20, 20)
        side_layout.setSpacing(6)

        title = QLabel(client.channel_name)
        title.setStyleSheet(style.FONT_TITLE)
        side_layout.addWidget(title)

        subtitle = QLabel("демо-режим · без токена")
        subtitle.setStyleSheet(style.FONT_SUBTITLE)
        side_layout.addWidget(subtitle)

        side_layout.addSpacing(16)

        # разделительная линия
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(
            f"background: {style.BORDER_SOFT}; max-height: 1px;"
        )
        side_layout.addWidget(line)

        side_layout.addSpacing(12)

        # список чатов
        chats = QListWidget()
        chats.setStyleSheet(
            f"QListWidget {{"
            f"  border: none;"
            f"  background: transparent;"
            f"  font-family: {style.FONT_FAMILY};"
            f"  font-size: 13px;"
            f"  color: {style.TEXT_PRIMARY};"
            f"}}"
            f"QListWidget::item {{"
            f"  padding: 9px 10px;"
            f"  border-radius: 6px;"
            f"}}"
            f"QListWidget::item:hover {{"
            f"  background: {style.BG_HOVER};"
            f"}}"
            f"QListWidget::item:selected {{"
            f"  background: {style.BG_SELECTED};"
            f"  color: {style.TEXT_PRIMARY};"
            f"}}"
        )

        for name in [
            client.channel_name,
            "Избранное",
            "Черновики",
        ]:
            chats.addItem(QListWidgetItem(name))
        chats.setCurrentRow(0)

        side_layout.addWidget(chats, stretch=1)

        # нижняя заметка
        note = QLabel(
            "Все данные синтетические.\n"
            "Реальные токены и ID не используются."
        )
        note.setWordWrap(True)
        note.setStyleSheet(
            f"{style.FONT_NOTE}"
            f"padding-top: 12px;"
            f"border-top: 1px solid {style.BORDER_SOFT};"
        )
        side_layout.addWidget(note)

        root.addWidget(sidebar)

        # ------------------------------------------------
        #  Правая панель
        # ------------------------------------------------
        right = QWidget()
        right.setStyleSheet(f"background: {style.BG_APP};")
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # шапка чата
        header = QFrame()
        header.setFixedHeight(64)
        header.setStyleSheet(
            f"QFrame {{"
            f"  background: {style.BG_HEADER};"
            f"  border-bottom: 1px solid {style.BORDER};"
            f"}}"
        )
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(24, 0, 24, 0)
        header_layout.setSpacing(14)

        h_title = QLabel(client.channel_name)
        h_title.setStyleSheet(style.FONT_TITLE)

        h_sep = QFrame()
        h_sep.setFrameShape(QFrame.VLine)
        h_sep.setStyleSheet(
            f"background: {style.BORDER_SOFT}; max-width: 1px;"
        )

        h_sub = QLabel("бот-навигатор по истории Горного Алтая")
        h_sub.setStyleSheet(style.FONT_SUBTITLE)

        header_layout.addWidget(h_title)
        header_layout.addWidget(h_sep)
        header_layout.addWidget(h_sub)
        header_layout.addStretch(1)

        right_layout.addWidget(header)

        # чат
        chat = ChatWidget(client)
        right_layout.addWidget(chat, stretch=1)

        root.addWidget(right, stretch=1)

        # статус-бар
        self.statusBar().setStyleSheet(
            f"QStatusBar {{"
            f"  background: {style.BG_SIDEBAR};"
            f"  color: {style.TEXT_MUTED};"
            f"  font-family: {style.FONT_FAMILY};"
            f"  font-size: 11px;"
            f"  border-top: 1px solid {style.BORDER};"
            f"}}"
        )
        self.statusBar().showMessage(
            "Демо-режим · канал «История Алтая БОТ» · без токена"
        )