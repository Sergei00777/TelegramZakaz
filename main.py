from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties  # ← Этот импорт обязателен!
import asyncio



# Импортируем конфиг
from config import BOT_TOKEN

# Импортируем роутеры из handlers
from handlers import start, catalog, cart, order, contacts, group_link, manager, help

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

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
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())