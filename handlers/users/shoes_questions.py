from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['about_shoes'])
async def about_shoes(message: types.Message):
    await message.reply(
        f'{str(get_headers()[23])}\n\n'
        f'{str(get_paragraphs()[23])}'
    )
