# handlers/manager.py
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# Кнопка с прямой ссылкой на менеджера @PSergei007
@router.message(lambda message: message.text == "💬 Связь с менеджером")
async def contact_manager(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👨‍💼 Написать менеджеру Сергей", url="https://t.me/PSergei007")]
    ])
    await message.answer(
        "📲 Нажмите кнопку ниже, чтобы написать менеджеру.\n"
        "Отвечаем быстро — в течение рабочего дня.",
        reply_markup=keyboard
    )