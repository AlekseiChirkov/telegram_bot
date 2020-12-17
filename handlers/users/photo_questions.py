from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['about_photo'])
async def about_photo(message: types.Message):
    await message.reply(
        f'{str(get_headers()[33])}\n\n'
        f'{str(get_paragraphs()[32])}'
    )


@dp.message_handler(commands=['photo_exp'])
async def photo_exp(message: types.Message):
    await message.reply(
        f'{str(get_headers()[34])}\n\n'
        f'{str(get_paragraphs()[33])}'
    )

