import asyncio
from codecs import encode
from aiogram import types
import json
bilets_bttns = types.InlineKeyboardMarkup(row_width=3)
emo_sq = ["🔲", "🔳"]
def get_buttons():
    with open("python/buttons/text_and_data.json", encoding="utf-8") as f:
        data = json.load(f)
        return data

bilets_bttns.add(*(types.InlineKeyboardButton(emo_sq[int(data[0]) % 2 ] + " " + data + " " + emo_sq[int(data[0]) % 2 ], callback_data=text) for text, data in get_buttons()["text_and_data"].items()))