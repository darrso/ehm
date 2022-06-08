from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import sys
sys.path.append("EHM")
from python.buttons.inline_bttns import bilets_bttns
from python.bilets_funcs import get_all_name_bilets


# /start
async def start_command(message: types.Message):
    await message.answer("Для перехода в меню - /menu"
    "\nСписок билетов - /bilets")

# /help
async def help_command(message: types.Message):
   await message.answer("/menu - главное меню")

# /menu
async def menu_command(message: types.Message):
    await message.answer("Добро пожаловать в меню!\nВыберите <b>номер билета (список билетов - /bilets):</b>", reply_markup=bilets_bttns)

# /bilets
async def get_all_bilets(message:types.Message):
    text = get_all_name_bilets() + "\nВернуться в меню - /menu"
    await message.answer(text, reply_markup=bilets_bttns)


def register_start_help_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(help_command, commands="help")
    dp.register_message_handler(menu_command, commands="menu")
    dp.register_message_handler(get_all_bilets, commands="bilets")