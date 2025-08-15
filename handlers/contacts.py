# handlers/contacts.py
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "📞 Контакты")
async def show_contacts(message: Message):
    text = (
        "📞 **Наши контакты**\n\n"
        "👨‍💼 Менеджер: [Сергей](https://t.me/PSergei007)\n"
        "📦 Доставка по РФ и СНГ\n"
        "🕒 График работы: Пн–Сб, 9:00–18:00\n"
        "📧 Email: parts@china-auto.ru\n"
        "💬 Пишите в любое время — ответим в рабочее время"
    )
    await message.answer(text, parse_mode="Markdown")