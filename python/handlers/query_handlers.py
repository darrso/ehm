from aiogram import types, Dispatcher
from aiogram.utils.exceptions import BadRequest
import sys

sys.path.append("EHM")
from python.bilets_funcs import get_bilet


async def return_bilet_q(query: types.CallbackQuery):
    data = get_bilet(query.data)
    text = f"Название билета - <b>{data['bilet_name']}</b>\n\n"
    for i in range(len(data["bilet_questions"])):
        try:
            text += f'<b>{data["bilet_questions"][i]}</b>' + '\n' + data["bilet_answers"][i] + "\n\n\n"
        except IndexError:
            text = "Error: билет сформирован неправильно."
    await query.message.answer(text)
    
    media = types.MediaGroup()
    for value in data["images"]:
        media.attach_photo(value)
    try:
        await query.message.answer_media_group(media)
    except BadRequest:
        pass

def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(return_bilet_q, lambda text: text.data[0:6] in 'bilet_')