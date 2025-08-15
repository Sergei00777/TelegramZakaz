# handlers/group_link.py
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# Кнопка с ссылкой на группу
@router.message(lambda message: message.text == "🔗 Перейти в Telegram-группу")
async def open_group(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Перейти в группу", url="https://t.me/your_autospares_group")]
    ])
    await message.answer(
        "Присоединяйтесь к нашей группе!\n"
        "Актуальные поступления, скидки и новости запчастей из Китая 🚗",
        reply_markup=keyboard
    )