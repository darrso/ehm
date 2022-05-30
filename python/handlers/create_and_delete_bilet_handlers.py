from audioop import add
from os import stat
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types.message import ContentType
import sys


sys.path.append("python")
from states.states_bot import NewBilet, DeleteBilet
from config import admin_id

sys.path.append("EHM")
from python.bilets_funcs import add_bilet_to_json, delete_bilet

# ________CREATE BILET__________

# START CREATING NEW BILET: STATE 0
async def add_new_bilet(message: types.Message):
    await message.answer("Введите название билета (или слово <b><i>отмена</i></b> для отмены создания билета).")
    await NewBilet.creating_1.set()

# GET NAME BILET: STATE 1
async def add_new_bilet_name_bilet(message: types.Message, state: FSMContext):
    await message.answer(f"Название билета - <b>{message.text}</b>\n\n"
        'Введите <b>вопросы</b> в билете. Как разделитель используйте символ ";" (если вопрос 1, не используйте разделитель).')
    await state.update_data(bilet_name=message.text.capitalize())
    await NewBilet.next()

# GET  QUESTIONS BILET: STATE 2
async def add_new_bilet_ques(message: types.Message, state: FSMContext):
    questions = message.text.split(";")
    data = "\n".join(questions)
    await message.answer('Ваши вопросы:\n'
    f'{data}\n\n'
    'Введите <b>ответы</b> на вопросы, разделите их символом ";" (если ответ 1, не испоользуйте разделитель)')
    await state.update_data(ques=questions)
    await NewBilet.next()


# GET ANSWERS: STATE 3
async def add_new_bilet_anss(message: types.Message, state: FSMContext):
    answers = message.text.split(";")
    data = "\n".join(answers)
    await message.answer('Ваши ответы на вопросы:\n'
    f'{data}\n\n'
    'Отправьте <b>изображение</b> или слово <b><i>"отмена"</i></b>.')
    await state.update_data(anss=answers)
    await NewBilet.next()

# STATE 4
async def add_new_bilet_anss(message: types.Message, state: FSMContext):
    answers = message.text.split(";")
    data = "\n".join(answers)
    await message.answer('Ваши ответы на вопросы:\n'
    f'{data}\n\nБилет успешно создан.\n\n/menu - главное меню')
    await state.update_data(anss=answers)
    add_bilet_to_json(await state.get_data(), None)
    await state.finish()


# CANCEL CREATING NEW BILET: STATE FINISH
async def cancel_creating(message: types.Message, state: FSMContext):
    await message.answer("Отмена.\n/menu - вернуться в меню.")
    await state.finish()


# ________DELETE BILET__________

async def start_delete_bilet(message: types.Message):
    await message.answer("Введите номер билета, который хотите удалить (или <b>отмена</b>).")
    await DeleteBilet.deleting_0.set()

async def get_number_bilet(message: types.Message, state: FSMContext):
    if delete_bilet(message.text):
        await message.answer("Успешно!\n/menu - вернуться в меню.")
        await state.finish()
    else:
        await message.answer("Ошибка! Попробуйте еще раз (или введите 'отмена').")


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(add_new_bilet, lambda message: message.from_user.id == admin_id, commands="create_new")
    dp.register_message_handler(cancel_creating, lambda message: message.text.lower() == 'отмена', state=[NewBilet.creating_1, NewBilet.creating_1, NewBilet.creating_2, NewBilet.creating_3, DeleteBilet.deleting_0])
    dp.register_message_handler(add_new_bilet_name_bilet, state=NewBilet.creating_1)
    dp.register_message_handler(add_new_bilet_ques, state=NewBilet.creating_2)
    dp.register_message_handler(add_new_bilet_anss, state=NewBilet.creating_3)
    dp.register_message_handler(start_delete_bilet, lambda message: message.from_user.id == admin_id, commands="delete_bilet")
    dp.register_message_handler(get_number_bilet, state=DeleteBilet.deleting_0)