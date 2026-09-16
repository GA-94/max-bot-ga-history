# История Алтая БОТ

Локальный бот-навигатор по истории Горного Алтая
с предпросмотром UI на PyQt5. Работает без токена.

## Установка (Windows 10)

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Запуск

    python main.py

## Команды

- /help  — справка
- /sites — все ссылки по разделам
- /list  — меню эпох

## Режим без токена

Бот использует MockMaxClient — синтетический эмулятор
MAX API. Никакие реальные токены и ID не используются.

## Переход в продакшен

Замените MockMaxClient на maxbot_chatbot_python.Bot
в main.py. Логика bot/handlers.py остаётся той же.