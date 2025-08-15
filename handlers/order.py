# handlers/order.py
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "✅ Оформление заказа")
async def start_order_process(message: Message):
    text = (
        "📝 Начинаем оформление заказа!\n\n"
        "Пожалуйста, введите:\n"
        "1. Ваше имя\n"
        "2. Телефон\n"
        "3. Адрес (регион, город)\n\n"
        "Доставка: СДЭК, Почта России, самовывоз\n"
        "Оплата: при получении или предоплата\n\n"
        "Пока что это тестовое сообщение. В дальнейшем здесь будет пошаговая форма."
    )
    await message.answer(text)