# handlers/catalog.py
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "📦 Каталог")
async def show_catalog(message: Message):
    text = (
        "📂 Выберите категорию запчастей:\n\n"
        "🔹 Ноускаты\n"
        "🔹 Фары\n"
        "🔹 Бампера\n"
        "🔹 Капоты, двери\n"
        "🔹 Двигатели\n"
        "🔹 Коробка передач"
    )
    await message.answer(text)