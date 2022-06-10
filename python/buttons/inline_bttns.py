from aiogram import types

from python.bilets_funcs import load_bilets

bilets_bttns = types.InlineKeyboardMarkup(row_width=3)
emo_sq = ["🔲", "🔳"]

bilets_bttns.add(*(types.InlineKeyboardButton(emo_sq[int(data[0]) % 2 ] + " " + data + " " + emo_sq[int(data[0]) % 2 ], callback_data=text) for text, data in load_bilets("python/buttons/text_and_data.json")["text_and_data"].items()))
