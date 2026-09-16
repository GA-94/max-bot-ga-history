# bot/config.py
"""
Конфигурация бота «История Алтая БОТ».
Все тексты и ссылки — здесь.
"""

BOT_NAME = "История Алтая БОТ"
CHANNEL_NAME = "История Алтая БОТ"

# ------------------------------------------------------------
#  /help
# ------------------------------------------------------------
HELP_TEXT = (
    "История Алтая БОТ\n"
    "─────────────────────────────\n\n"
    "Навигатор по истории Горного Алтая.\n"
    "Подскажу, где искать материалы.\n\n"
    "Доступные команды:\n\n"
    "  /help    эта справка\n"
    "  /sites   список ссылок по разделам\n"
    "  /list    краткое меню эпох"
)

# ------------------------------------------------------------
#  /list
# ------------------------------------------------------------
LIST_TEXT = (
    "Горный Алтай в древности\n"
    "Каменный век в истории Горного Алтая\n"
    "─────────────────────────────\n\n"
    "Меню:\n\n"
    "  01.  Общий обзор\n"
    "  02.  Палеолит — Улалинская стоянка\n"
    "  03.  Мезолит\n"
    "  04.  Неолит\n"
    "  05.  Энеолит (медно-каменный век)\n"
    "  06.  Эпоха бронзы\n\n"
    "Полный список ссылок — команда /sites"
)

# ------------------------------------------------------------
#  /sites
# ------------------------------------------------------------
SITES_TEXT = (
    "Горный Алтай в древности\n"
    "Каменный век в истории Горного Алтая\n"
    "─────────────────────────────\n\n"

    "Общий обзор\n"
    "· https://yandex.ru/video/preview/16726963929669204292"
    "?text=палеолит%20в%20горном%20алтае"
    "&path=yandex_search"
    "&parent-reqid=1788253581454904-7773433489822030927"
    "-balancer-l7leveler-kubr-yp-klg-66-BAL"
    "&from_type=vast\n"
    "· https://www.musey-anohina.ru/index.php/2014-01-20-22-52-62\n\n"

    "Палеолит\n"
    "· Улалинская стоянка\n"
    "  https://www.musey-anohina.ru/index.php/yubilei/item/"
    "1449-60-let-nazad-byla-otkryta-ulalinskaya-stoyanka\n"
    "· Опыт создания периодизации каменного века Алтая\n"
    "  https://cyberleninka.ru/article/n/"
    "opyt-sozdaniya-periodizatsii-kamennogo-veka-altaya\n"
    "· http://archaeology.asu.ru/portal/Палеолит\n\n"

    "Мезолит\n"
    "· https://cyberleninka.ru/article/n/"
    "problemy-issledovaniya-mezolita-altaya"
    "?ysclid=mtigabehvi96906428\n\n"

    "Неолит\n"
    "· Современные концепции культурной принадлежности "
    "поселенческих комплексов неолита Алтая\n"
    "  https://cyberleninka.ru/article/n/"
    "sovremennye-kontseptsii-kulturnoy-prinadlezhnosti-"
    "poselencheskih-kompleksov-neolita-altaya\n\n"

    "Энеолит (медно-каменный век)\n"
    "· http://old.archaeology.nsc.ru/ru/otdel/noo/noo15.aspx\n"
    "· История Алтая\n"
    "  http://irbis.akunb.altlib.ru:81/bv/bv000238.pdf\n\n"

    "Эпоха бронзы\n"
    "· http://elib.nbra.ru/bd/pdf_new/8/459.pdf\n"
    "· http://elib.nbra.ru/bd/pdf_new/8/458.pdf"
)

# ------------------------------------------------------------
#  Структурированные данные (для инлайн-кнопок в будущем)
# ------------------------------------------------------------
SECTIONS = {
    "overview": {
        "title": "Общий обзор",
        "links": [
            (
                "Яндекс.Видео — палеолит в Горном Алтае",
                "https://yandex.ru/video/preview/16726963929669204292"
                "?text=палеолит%20в%20горном%20алтае"
                "&path=yandex_search"
                "&parent-reqid=1788253581454904-7773433489822030927"
                "-balancer-l7leveler-kubr-yp-klg-66-BAL"
                "&from_type=vast",
            ),
            (
                "Музей Анохина",
                "https://www.musey-anohina.ru/index.php/2014-01-20-22-52-62",
            ),
        ],
    },
    "paleolit": {
        "title": "Палеолит",
        "links": [
            (
                "Улалинская стоянка",
                "https://www.musey-anohina.ru/index.php/yubilei/item/"
                "1449-60-let-nazad-byla-otkryta-ulalinskaya-stoyanka",
            ),
            (
                "Опыт создания периодизации каменного века Алтая",
                "https://cyberleninka.ru/article/n/"
                "opyt-sozdaniya-periodizatsii-kamennogo-veka-altaya",
            ),
            (
                "Археология АГУ — Палеолит",
                "http://archaeology.asu.ru/portal/Палеолит",
            ),
        ],
    },
    "mezolit": {
        "title": "Мезолит",
        "links": [
            (
                "Проблемы исследования мезолита Алтая",
                "https://cyberleninka.ru/article/n/"
                "problemy-issledovaniya-mezolita-altaya"
                "?ysclid=mtigabehvi96906428",
            ),
        ],
    },
    "neolit": {
        "title": "Неолит",
        "links": [
            (
                "Современные концепции культурной принадлежности "
                "поселенческих комплексов неолита Алтая",
                "https://cyberleninka.ru/article/n/"
                "sovremennye-kontseptsii-kulturnoy-prinadlezhnosti-"
                "poselencheskih-kompleksov-neolita-altaya",
            ),
        ],
    },
    "eneolit": {
        "title": "Энеолит (медно-каменный век)",
        "links": [
            (
                "Институт археологии СО РАН",
                "http://old.archaeology.nsc.ru/ru/otdel/noo/noo15.aspx",
            ),
            (
                "История Алтая (PDF)",
                "http://irbis.akunb.altlib.ru:81/bv/bv000238.pdf",
            ),
        ],
    },
    "bronza": {
        "title": "Эпоха бронзы",
        "links": [
            (
                "НБРА — PDF (459)",
                "http://elib.nbra.ru/bd/pdf_new/8/459.pdf",
            ),
            (
                "НБРА — PDF (458)",
                "http://elib.nbra.ru/bd/pdf_new/8/458.pdf",
            ),
        ],
    },
}