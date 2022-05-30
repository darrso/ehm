import asyncio
import logging

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from python.config import bToken
from python.handlers.create_and_delete_bilet_handlers import register_message_handlers
from python.handlers.query_handlers import register_query_handlers
from python.handlers.defolt_commands import register_start_help_commands
from python.handlers.add_photos_handlers import register_add_photos_handlers

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bToken, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())

async def main():
    bot = Bot(token=bToken, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())
    await bot.set_my_commands([BotCommand(command="/start", description="Запуск бота"),
    BotCommand("create_new", description="Создать новый билет"), BotCommand("menu", "Главное меню"), BotCommand("bilets", "Посмотреть список билетов"),
    BotCommand("add_photos", "Добавить билеты"), BotCommand("delete_bilet", "Удалить билет")]) 
    
    register_message_handlers(dp)
    register_query_handlers(dp)
    register_start_help_commands(dp)
    register_add_photos_handlers(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
