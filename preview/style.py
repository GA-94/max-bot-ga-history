# preview/style.py
"""
Единая палитра и типографика.
Без эмодзи — только сдержанные цвета и отступы.
"""

# ---------- палитра ----------
BG_APP        = "#ffffff"
BG_SIDEBAR    = "#fafafa"
BG_HEADER     = "#ffffff"
BG_FEED       = "#ffffff"
BG_INPUT      = "#ffffff"
BG_HOVER      = "#f5f5f5"
BG_SELECTED   = "#eeeeee"

BORDER        = "#e8e8e8"
BORDER_SOFT   = "#f0f0f0"

TEXT_PRIMARY  = "#1a1a1a"
TEXT_SECOND   = "#6b6b6b"
TEXT_MUTED    = "#9a9a9a"
TEXT_INVERT   = "#ffffff"

# ---------- акценты по авторам ----------
BUBBLE_BOT_BG     = "#f4f6f8"
BUBBLE_BOT_BRD    = "#e3e8ee"
BUBBLE_BOT_ACCENT = "#3a6ea5"

BUBBLE_USER_BG    = "#f2f7f4"
BUBBLE_USER_BRD   = "#dfeae2"
BUBBLE_USER_ACCENT= "#3f7d5b"

BUBBLE_SYS_BG     = "#f7f7f7"
BUBBLE_SYS_BRD    = "#ececec"
BUBBLE_SYS_ACCENT = "#8a8a8a"

ACCENT_BUTTON     = "#2b2b2b"
ACCENT_BUTTON_HOV = "#000000"

# ---------- типографика ----------
FONT_FAMILY = "Segoe UI, Inter, sans-serif"

FONT_TITLE    = f"font-family: {FONT_FAMILY}; font-size: 15px; " \
                f"font-weight: 600; color: {TEXT_PRIMARY};"
FONT_SUBTITLE = f"font-family: {FONT_FAMILY}; font-size: 11px; " \
                f"color: {TEXT_MUTED};"
FONT_AUTHOR   = f"font-family: {FONT_FAMILY}; font-size: 11px; " \
                f"font-weight: 600;"
FONT_BODY     = f"font-family: {FONT_FAMILY}; font-size: 13px; " \
                f"color: {TEXT_PRIMARY};"
FONT_TIME     = f"font-family: {FONT_FAMILY}; font-size: 10px; " \
                f"color: {TEXT_MUTED};"
FONT_NOTE     = f"font-family: {FONT_FAMILY}; font-size: 11px; " \
                f"color: {TEXT_MUTED};"

# ---------- радиусы и отступы ----------
RADIUS_BUBBLE = 10
RADIUS_INPUT  = 8
PAD_BUBBLE    = (14, 10, 14, 10)
GAP_BUBBLES   = 8