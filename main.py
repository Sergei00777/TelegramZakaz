from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# Импортируем конфиг
from config import BOT_TOKEN

# Импортируем роутеры из handlers
from handlers import start, catalog, cart, order, contacts, group_link, manager, help

# Создаём хранилище для FSM (Finite State Machine)
storage = MemoryStorage()

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)

# Подключаем роутеры
dp.include_router(start.router)
dp.include_router(catalog.router)
dp.include_router(cart.router)
dp.include_router(order.router)
dp.include_router(contacts.router)
dp.include_router(group_link.router)
dp.include_router(manager.router)
dp.include_router(help.router)

# Запуск бота
async def main():
    print("🤖 Бот запущен...")
    print("📊 FSM хранилище инициализировано")
    print("🔄 Ожидание сообщений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())