# handlers/cart.py
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "🛒 Корзина")
async def show_cart(message: Message):
    # Пока корзина пуста — заглушка
    text = (
        "🛒 Ваша корзина пуста\n\n"
        "Чтобы добавить товар — используйте поиск или каталог."
    )
    await message.answer(text)