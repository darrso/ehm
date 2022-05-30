from aiogram.types.message import ContentType
import sys
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
sys.path.append("EHM")
from python.buttons.inline_bttns import bilets_bttns
from python.states.states_bot import AddPhoto
from python.bilets_funcs import add_photo_to_json
from python.config import admin_id

async def add_photo_start(message: types.Message):
    await message.answer("Вы решили добавить фото в билет. Выберите его номер: ", reply_markup=bilets_bttns)
    await AddPhoto.adding_0.set()

async def add_photo_save_choosen_bilet(query: types.CallbackQuery, state: FSMContext):
    data = query.data[-1]
    await query.answer(f"Вы выбрали билет № {data}")
    await query.message.answer('Отправьте изображения, которые хотите добавить в билет.\nКогда закончите, отправьте - "стоп"')
    await state.update_data(number=data)
    await AddPhoto.next()

async def get_photos(message: types.Message, state: FSMContext):
    image = message.photo[0].file_id
    number = await state.get_data()
    add_photo_to_json(image, number["number"])

async def stop_getting_photos(message: types.Message, state: FSMContext):
    await message.answer("Конец сохранения изображений!\n\n/menu - главное меню")
    await state.finish()

def register_add_photos_handlers(dp: Dispatcher):
    dp.register_message_handler(add_photo_start, lambda message: message.from_user.id == admin_id, commands="add_photos")
    dp.register_callback_query_handler(add_photo_save_choosen_bilet, lambda text: text.data[0:6] in 'bilet_', state=AddPhoto.adding_0)
    dp.register_message_handler(get_photos, state=AddPhoto.adding_1, content_types=[ContentType.PHOTO])
    dp.register_message_handler(stop_getting_photos, lambda message: message.text.lower() == "стоп", state=AddPhoto.adding_1)