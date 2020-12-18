from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['about_industrial'])
async def about_industrial(message: types.Message):
    await message.reply(
        f'{str(get_headers()[52])}\n\n'
        f'{str(get_paragraphs()[51])}'
    )
