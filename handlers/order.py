# handlers/order.py
from aiogram import Router
from aiogram.types import Message

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import datetime
import random

router = Router()


# Определяем состояния для FSM
class OrderState(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_city = State()
    waiting_for_part = State()
    waiting_for_car_number = State()
    waiting_for_confirm = State()


# ID менеджера (замените на реальный)
MANAGER_ID = 6997654564


# Генерация номера заказа
def generate_order_number():
    return f"ORD-{datetime.datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"


# Клавиатура для отмены
def get_cancel_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="❌ Отменить заказ")]],
        resize_keyboard=True
    )


# Клавиатура для подтверждения
def get_confirm_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Подтвердить заказ")],
            [KeyboardButton(text="❌ Отменить")]
        ],
        resize_keyboard=True
    )


# Начало оформления заказа
@router.message(F.text == "✅ Оформление заказа")
async def start_order_process(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        "📝 Начинаем оформление заказа!\n\n"
        "Пожалуйста, введите ваше имя:",
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(OrderState.waiting_for_name)


# Обработка имени
@router.message(OrderState.waiting_for_name, F.text != "❌ Отменить заказ")
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(
        "📞 Теперь введите ваш телефонный номер:\n\n"
        "Пример: +79123456789 или 89123456789",
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(OrderState.waiting_for_phone)


# Обработка телефона
@router.message(OrderState.waiting_for_phone, F.text != "❌ Отменить заказ")
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    await message.answer(
        "🏙️ Введите ваш город:",
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(OrderState.waiting_for_city)


# Обработка города
@router.message(OrderState.waiting_for_city, F.text != "❌ Отменить заказ")
async def process_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)

    await message.answer(
        "🔧 Опишите, какую запчасть нужно заказать:\n\n"
        "Пример: 'Передний бампер на Toyota Camry 2015 года'",
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(OrderState.waiting_for_part)


# Обработка описания запчасти
@router.message(OrderState.waiting_for_part, F.text != "❌ Отменить заказ")
async def process_part(message: Message, state: FSMContext):
    await state.update_data(part_description=message.text)

    await message.answer(
        "🚗 Введите госномер автомобиля (если известен):\n\n"
        "Пример: А123ВС77 или оставьте пустым",
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(OrderState.waiting_for_car_number)


# Обработка госномера
@router.message(OrderState.waiting_for_car_number)
async def process_car_number(message: Message, state: FSMContext):
    car_number = message.text if message.text != "❌ Отменить заказ" else "Не указан"
    await state.update_data(car_number=car_number)

    # Получаем все данные
    data = await state.get_data()

    # Формируем сводку заказа
    order_summary = (
        "📋 Пожалуйста, проверьте данные заказа:\n\n"
        f"👤 Имя: {data.get('name', 'Не указано')}\n"
        f"📞 Телефон: {data.get('phone', 'Не указан')}\n"
        f"🏙️ Город: {data.get('city', 'Не указан')}\n"
        f"🚗 Госномер: {data.get('car_number', 'Не указан')}\n"
        f"🔧 Запчасть: {data.get('part_description', 'Не указана')}\n\n"
        "✅ Все верно? Подтвердите заказ:"
    )

    await message.answer(
        order_summary,
        reply_markup=get_confirm_keyboard()
    )
    await state.set_state(OrderState.waiting_for_confirm)


# Подтверждение заказа
@router.message(OrderState.waiting_for_confirm, F.text == "✅ Подтвердить заказ")
async def confirm_order(message: Message, state: FSMContext):
    data = await state.get_data()
    order_number = generate_order_number()

    # Сообщение для пользователя
    user_message = (
            f"🎉 Заказ #{order_number} оформлен!\n\n"
            "✅ Ваш заказ принят в обработку.\n"
            "📞 Менеджер свяжется с вами в течение 15 минут.\n"
            "⏰ Время оформления: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    )

    # Сообщение для менеджера
    manager_message = (
        f"🚨 НОВЫЙ ЗАКАЗ #{order_number}\n\n"
        f"👤 Клиент: {data.get('name', 'Не указано')}\n"
        f"📞 Телефон: {data.get('phone', 'Не указан')}\n"
        f"🏙️ Город: {data.get('city', 'Не указан')}\n"
        f"🚗 Госномер: {data.get('car_number', 'Не указан')}\n"
        f"🔧 Запчасть: {data.get('part_description', 'Не указана')}\n"
        f"⏰ Время: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        f"👤 ID пользователя: {message.from_user.id}"
    )

    await message.answer(user_message, reply_markup=ReplyKeyboardRemove())

    # Отправляем уведомление менеджеру
    try:
        await message.bot.send_message(
            chat_id=MANAGER_ID,
            text=manager_message
        )
    except Exception as e:
        print(f"Ошибка отправки менеджеру: {e}")
        await message.answer(
            "⚠️ Не удалось отправить уведомление менеджеру. "
            "Пожалуйста, свяжитесь с нами по телефону."
        )

    await state.clear()


# Отмена заказа на любом этапе
@router.message(StateFilter(OrderState), F.text == "❌ Отменить заказ")
@router.message(OrderState.waiting_for_confirm, F.text == "❌ Отменить")
async def cancel_order(message: Message, state: FSMContext):
    await message.answer(
        "❌ Оформление заказа отменено.",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


# Обработка некорректных сообщений
@router.message(StateFilter(OrderState))
async def process_incorrect_input(message: Message):
    await message.answer(
        "Пожалуйста, используйте кнопки для продолжения оформления заказа.",
        reply_markup=get_cancel_keyboard()
    )