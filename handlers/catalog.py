# handlers/catalog.py
from aiogram import Router
from aiogram.types import Message

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Импортируем главное меню
from keyboards.main_menu import get_main_menu

router = Router()

# Создаем клавиатуру с кнопками категорий
def get_catalog_keyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [
        "🔹 Бампера",
        "🔹 Фары",
        "🔹 Капоты",
        "🔹 Двери",
        "🔹 Двигатели",
        "🔹 КПП",
        "🔹 Назад"
    ]
    for button in buttons:
        builder.add(KeyboardButton(text=button))
    builder.adjust(2)  # 2 кнопки в ряду
    return builder.as_markup(resize_keyboard=True)

# Обработчик кнопки "Каталог"
@router.message(F.text == "📦 Каталог")
async def show_catalog(message: Message):
    await message.answer(
        "📂 Выберите категорию запчастей:",
        reply_markup=get_catalog_keyboard()
    )

# Обработчики для каждой категории
@router.message(F.text == "🔹 Бампера")
async def show_bumpers_info(message: Message):
    info = """
🔹 **БАМПЕРА**

💵 **Цена:** от 5 000 до 25 000 руб.
📦 **Наличие:** 47 шт. на складе
🚚 **Срок поставки:** 1-3 дня
🔧 **Состояние:** б/у, оригинал
📋 **Применяемость:** все марки авто

_Подробности уточняйте у менеджера_
    """
    await message.answer(info)

@router.message(F.text == "🔹 Фары")
async def show_lights_info(message: Message):
    info = """
🔹 **ФАРЫ**

💵 **Цена:** от 3 000 до 40 000 руб.
📦 **Наличие:** 32 шт. на складе  
🚚 **Срок поставки:** 2-4 дня
🔧 **Состояние:** новые и б/у
⚡ **Тип:** галоген, ксенон, LED

_Возможна установка в сервисе_
    """
    await message.answer(info)

@router.message(F.text == "🔹 Капоты")
async def show_hoods_info(message: Message):
    info = """
🔹 **КАПОТЫ**

💵 **Цена:** от 8 000 до 50 000 руб.
📦 **Наличие:** 15 шт. на складе
🚚 **Срок поставка:** 3-5 дней
🔧 **Материал:** сталь, алюминий
🎨 **Цвет:** под покраску

_Подбор по VIN-коду_
    """
    await message.answer(info)

@router.message(F.text == "🔹 Двери")
async def show_doors_info(message: Message):
    info = """
🔹 **ДВЕРИ**

💵 **Цена:** от 7 000 до 35 000 руб.
📦 **Наличие:** 28 шт. на складе
🚚 **Срок поставки:** 2-4 дня
🔧 **Комплектация:** с стеклом и обшивкой
🚪 **Тип:** передние, задние

_Полная комплектация_
    """
    await message.answer(info)

@router.message(F.text == "🔹 Двигатели")
async def show_engines_info(message: Message):
    info = """
🔹 **ДВИГАТЕЛИ**

💵 **Цена:** от 40 000 до 250 000 руб.
📦 **Наличие:** 12 шт. на складе
🚚 **Срок поставки:** 5-7 дней
⚙ **Тип:** бензин, дизель
🔧 **Состояние:** контрактные, б/у

_Гарантия 30 дней_
    """
    await message.answer(info)

@router.message(F.text == "🔹 КПП")
async def show_gearbox_info(message: Message):
    info = """
🔹 **КОРОБКА ПЕРЕДАЧ (КПП)**

💵 **Цена:** от 20 000 до 150 000 руб.
📦 **Наличие:** 18 шт. на складе
🚚 **Срок поставки:** 4-6 дней
⚙ **Тип:** МКПП, АКПП, вариатор
🔧 **Состояние:** контрактные

_Тестирование перед покупкой_
    """
    await message.answer(info)

# Обработчик кнопки "Назад" для возврата в главное меню
@router.message(F.text == "🔹 Назад")
async def back_to_main(message: Message):
    await message.answer(
        "Возвращаемся в главное меню:",
        reply_markup=get_main_menu()
    )