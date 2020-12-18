from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['about_tobacco'])
async def about_tobacco(message: types.Message):
    await message.reply(
        f'{str(get_headers()[11])}\n\n'
        f'{str(get_paragraphs()[11])}'
    )


@dp.message_handler(commands=['rules_tobacco'])
async def rules_tobacco(message: types.Message):
    await message.reply(
        f'{str(get_headers()[12])}\n\n'
        f'{str(get_paragraphs()[12])}'
    )
