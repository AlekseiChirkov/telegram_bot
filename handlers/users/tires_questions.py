from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['about_tires'])
async def about_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[35])}\n\n'
        f'{str(get_paragraphs()[34])}'
    )


@dp.message_handler(commands=['tires_exp'])
async def tires_exp(message: types.Message):
    await message.reply(
        f'{str(get_headers()[36])}\n\n'
        f'{str(get_paragraphs()[35])}'
    )


@dp.message_handler(commands=['registration_tires'])
async def registration_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[37])}\n\n'
        f'{str(get_paragraphs()[36])}'
    )


@dp.message_handler(commands=['description_tires'])
async def description_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[38])}\n\n'
        f'{str(get_paragraphs()[37])}'
    )


@dp.message_handler(commands=['payment_tires'])
async def payment_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[39])}\n\n'
        f'{str(get_paragraphs()[38])}'
    )


@dp.message_handler(commands=['ordering_tires'])
async def ordering_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[40])}\n\n'
        f'{str(get_paragraphs()[39])}'
    )


@dp.message_handler(commands=['turnover_tires'])
async def turnover_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[41])}\n\n'
        f'{str(get_paragraphs()[40])}'
    )


@dp.message_handler(commands=['ede_tires'])
async def ede_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[42])}\n\n'
        f'{str(get_paragraphs()[41])}'
    )


@dp.message_handler(commands=['withdrawal_tires'])
async def withdrawal_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[43])}\n\n'
        f'{str(get_paragraphs()[42])}'
    )


@dp.message_handler(commands=['return_tires'])
async def return_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[45])}\n\n'
        f'{str(get_paragraphs()[44])}'
    )


@dp.message_handler(commands=['remarking_tires'])
async def remarking_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[46])}\n\n'
        f'{str(get_paragraphs()[45])}'
    )


@dp.message_handler(commands=['aggregation_tires'])
async def aggregation_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[47])}\n\n'
        f'{str(get_paragraphs()[46])}'
    )


@dp.message_handler(commands=['documentation_tires'])
async def documentation_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[48])}\n\n'
        f'{str(get_paragraphs()[47])}'
    )


@dp.message_handler(commands=['wholesale_tires'])
async def wholesale_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[49])}\n\n'
        f'{str(get_paragraphs()[48])}'
    )


@dp.message_handler(commands=['import_tires'])
async def import_tires(message: types.Message):
    await message.reply(
        f'{str(get_headers()[50])}\n\n'
        f'{str(get_paragraphs()[49])}'
    )


