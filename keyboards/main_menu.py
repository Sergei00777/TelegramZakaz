# keyboards/main_menu.py
from aiogram import types

def get_main_menu():
    keyboard = [
        [types.KeyboardButton(text="📦 Каталог")],
        [types.KeyboardButton(text="🛒 Корзина")],
        [types.KeyboardButton(text="✅ Оформление заказа")],
        [types.KeyboardButton(text="📞 Контакты")],
        [types.KeyboardButton(text="🔗 Перейти в Telegram-группу")],
        [types.KeyboardButton(text="💬 Связь с менеджером")],
        [types.KeyboardButton(text="ℹ️ Справка")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)