# handlers/start.py
from aiogram import Router, types
from aiogram.filters import CommandStart

from keyboards.main_menu import get_main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "👋 Привет! Я — ваш помощник в подборе автозапчастей из Китая.\n\n"
        "🔧 В наличии и под заказ:\n"
        "▪️ Ноускаты ▪️ Фары ▪️ Бампера\n"
        "▪️ Капоты, двери ▪️ Двигатели ▪️ Коробка передач\n\n"
        "💸 Экономьте до 40% без потери качества\n"
        "🛠 Гарантия на все запчасти\n"
        "🚚 Быстрая доставка по РФ и СНГ\n\n"
        "📲 Выберите действие ниже:"
    )
    await message.answer(text, reply_markup=get_main_menu())