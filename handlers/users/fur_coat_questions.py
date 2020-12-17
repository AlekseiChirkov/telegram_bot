from aiogram import types

from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.message_handler(commands=['about_fur_coat'])
async def about_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[13])}\n\n'
        f'{str(get_paragraphs()[13])}'
    )


@dp.message_handler(commands=['register_fur_coat'])
async def register_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[14])}\n\n'
        f'{str(get_paragraphs()[14])}'
    )


@dp.message_handler(commands=['describe_fur_coat'])
async def describe_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[15])}\n\n'
        f'{str(get_paragraphs()[15])}'
    )


@dp.message_handler(commands=['order_fur_coat'])
async def order_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[16])}\n\n'
        f'{str(get_paragraphs()[16])}'
    )


@dp.message_handler(commands=['label_fur_coat'])
async def label_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[17])}\n\n'
        f'{str(get_paragraphs()[17])}'
    )


@dp.message_handler(commands=['requirements_fur_coat'])
async def requirements_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[18])}\n\n'
        f'{str(get_paragraphs()[18])}'
    )


@dp.message_handler(commands=['import_fur_coat'])
async def import_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[19])}\n\n'
        f'{str(get_paragraphs()[19])}'
    )


@dp.message_handler(commands=['shipping_fur_coat'])
async def shipping_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[20])}\n\n'
        f'{str(get_paragraphs()[20])}'
    )


@dp.message_handler(commands=['retail_fur_coat'])
async def retail_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[21])}\n\n'
        f'{str(get_paragraphs()[21])}'
    )


@dp.message_handler(commands=['badge_damaged_fur_coat'])
async def badge_damaged_fur_coat(message: types.Message):
    await message.reply(
        f'{str(get_headers()[22])}\n\n'
        f'{str(get_paragraphs()[22])}'
    )
