from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['medicine_exp'])
async def medicine_exp(message: types.Message):
    await message.reply(
        f'{str(get_headers()[25])}\n\n'
        f'{str(get_paragraphs()[24])}'
    )


@dp.message_handler(commands=['account'])
async def account(message: types.Message):
    await message.reply(
        f'{str(get_headers()[26])}\n\n'
        f'{str(get_paragraphs()[25])}'
    )


@dp.message_handler(commands=['emissions'])
async def emissions(message: types.Message):
    await message.reply(
        f'{str(get_headers()[27])}\n\n'
        f'{str(get_paragraphs()[26])}'
    )


@dp.message_handler(commands=['disposal'])
async def disposal(message: types.Message):
    await message.reply(
        f'{str(get_headers()[28])}\n\n'
        f'{str(get_paragraphs()[27])}'
    )


@dp.message_handler(commands=['digital_code'])
async def digital_code(message: types.Message):
    await message.reply(
        f'{str(get_headers()[29])}\n\n'
        f'{str(get_paragraphs()[28])}'
    )


@dp.message_handler(commands=['equipment'])
async def equipment(message: types.Message):
    await message.reply(
        f'{str(get_headers()[30])}\n\n'
        f'{str(get_paragraphs()[29])}'
    )


@dp.message_handler(commands=['basic_actions'])
async def basic_actions(message: types.Message):
    await message.reply(
        f'{str(get_headers()[31])}\n\n'
        f'{str(get_paragraphs()[30])}'
    )


@dp.message_handler(commands=['automation'])
async def automation(message: types.Message):
    await message.reply(
        f'{str(get_headers()[32])}\n\n'
        f'{str(get_paragraphs()[31])}'
    )
