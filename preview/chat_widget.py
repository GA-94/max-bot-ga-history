# preview/chat_widget.py
"""
Компонент «чат»: лента сообщений и строка ввода.
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
    QSizePolicy,
)

from bot.mock_client import MockMaxClient, Message
from . import style


class MessageBubble(QFrame):
    """Один пузырь сообщения."""

    STYLES = {
        "bot": (
            f"QFrame {{ background: {style.BUBBLE_BOT_BG}; "
            f"border: 1px solid {style.BUBBLE_BOT_BRD}; "
            f"border-radius: {style.RADIUS_BUBBLE}px; }}"
        ),
        "user": (
            f"QFrame {{ background: {style.BUBBLE_USER_BG}; "
            f"border: 1px solid {style.BUBBLE_USER_BRD}; "
            f"border-radius: {style.RADIUS_BUBBLE}px; }}"
        ),
        "system": (
            f"QFrame {{ background: {style.BUBBLE_SYS_BG}; "
            f"border: 1px solid {style.BUBBLE_SYS_BRD}; "
            f"border-radius: {style.RADIUS_BUBBLE}px; }}"
        ),
    }

    AUTHORS = {
        "bot":    ("Бот",     style.BUBBLE_BOT_ACCENT),
        "user":   ("Вы",      style.BUBBLE_USER_ACCENT),
        "system": ("Система", style.BUBBLE_SYS_ACCENT),
    }

    def __init__(self, msg: Message, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet(
            self.STYLES.get(msg.author, self.STYLES["system"])
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(*style.PAD_BUBBLE)
        layout.setSpacing(4)

        # метка автора
        name, accent = self.AUTHORS.get(msg.author, ("—", style.TEXT_MUTED))
        author = QLabel(name.upper())
        author.setStyleSheet(
            f"{style.FONT_AUTHOR} color: {accent}; "
            f"letter-spacing: 0.5px;"
        )

        # тело сообщения
        text = QLabel(msg.text)
        text.setWordWrap(True)
        text.setTextInteractionFlags(
            Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse
        )
        text.setOpenExternalLinks(True)
        text.setStyleSheet(style.FONT_BODY)

        # время
        time = QLabel(msg.time.strftime("%H:%M"))
        time.setStyleSheet(style.FONT_TIME)
        time.setAlignment(Qt.AlignRight)

        layout.addWidget(author)
        layout.addWidget(text)
        layout.addWidget(time)


class ChatWidget(QWidget):
    """Лента сообщений и строка ввода."""

    def __init__(self, client: MockMaxClient, parent=None):
        super().__init__(parent)
        self.client = client

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ---------- лента ----------
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet(
            f"QScrollArea {{ border: none; background: {style.BG_FEED}; }}"
        )

        self.feed = QWidget()
        self.feed.setStyleSheet(f"background: {style.BG_FEED};")
        self.feed_layout = QVBoxLayout(self.feed)
        self.feed_layout.setContentsMargins(24, 20, 24, 20)
        self.feed_layout.setSpacing(style.GAP_BUBBLES)
        self.feed_layout.addStretch(1)

        self.scroll.setWidget(self.feed)
        root.addWidget(self.scroll, stretch=1)

        # ---------- строка ввода ----------
        input_row = QHBoxLayout()
        input_row.setContentsMargins(20, 12, 20, 16)
        input_row.setSpacing(10)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Сообщение — /help, /sites, /list")
        self.input.setStyleSheet(
            f"QLineEdit {{"
            f"  padding: 10px 14px;"
            f"  background: {style.BG_INPUT};"
            f"  border: 1px solid {style.BORDER};"
            f"  border-radius: {style.RADIUS_INPUT}px;"
            f"  font-family: {style.FONT_FAMILY};"
            f"  font-size: 13px;"
            f"  color: {style.TEXT_PRIMARY};"
            f"}}"
            f"QLineEdit:focus {{"
            f"  border: 1px solid {style.BUBBLE_BOT_ACCENT};"
            f"}}"
        )
        self.input.returnPressed.connect(self._on_send)

        send_btn = QPushButton("Отправить")
        send_btn.setCursor(Qt.PointingHandCursor)
        send_btn.setStyleSheet(
            f"QPushButton {{"
            f"  padding: 10px 18px;"
            f"  background: {style.ACCENT_BUTTON};"
            f"  color: {style.TEXT_INVERT};"
            f"  border: none;"
            f"  border-radius: {style.RADIUS_INPUT}px;"
            f"  font-family: {style.FONT_FAMILY};"
            f"  font-size: 13px;"
            f"  font-weight: 500;"
            f"}}"
            f"QPushButton:hover {{ background: {style.ACCENT_BUTTON_HOV}; }}"
        )
        send_btn.clicked.connect(self._on_send)

        input_row.addWidget(self.input, stretch=1)
        input_row.addWidget(send_btn)
        root.addLayout(input_row)

        # ---------- подписка ----------
        self.client.subscribe(self._rebuild)
        self._rebuild()

    # ---------- внутреннее ----------
    def _on_send(self) -> None:
        text = self.input.text().strip()
        if not text:
            return
        self.input.clear()
        self.client.send_from_user(text)

    def _rebuild(self) -> None:
        while self.feed_layout.count() > 1:
            item = self.feed_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        for msg in self.client.messages:
            bubble = MessageBubble(msg)
            bubble.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Maximum
            )
            self.feed_layout.insertWidget(
                self.feed_layout.count() - 1, bubble
            )

        bar = self.scroll.verticalScrollBar()
        bar.setValue(bar.maximum())