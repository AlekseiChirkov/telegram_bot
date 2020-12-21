from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_main_buttons import category_main_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text="what_for")
async def main_questions(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[0])}\n\n'
        f'{str(get_paragraphs()[0])}',
        reply_markup=category_main_choice,
    )


@dp.message_handler(commands=['for_whom'])
async def for_whom(message: types.Message):
    await message.reply(
        f'{str(get_headers()[1])}\n\n'
        f'{str(get_paragraphs()[1])}'
    )


@dp.message_handler(commands=['work_process'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[2])}\n\n'
        f'{str(get_paragraphs()[2])}'
    )


@dp.message_handler(commands=['fake'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[3])}\n\n'
        f'{str(get_paragraphs()[3])}'
    )


@dp.message_handler(commands=['who_marks'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[4])}\n\n'
        f'{str(get_paragraphs()[4])}'
    )


@dp.message_handler(commands=['make_fake'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[5])}\n\n'
        f'{str(get_paragraphs()[5])}'
    )


@dp.message_handler(commands=['who_response'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[6])}\n\n'
        f'{str(get_paragraphs()[6])}'
    )


@dp.message_handler(commands=['what_goods'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[8])}\n\n'
        f'{str(get_paragraphs()[8])}'
    )


@dp.message_handler(commands=['price_growth'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[9])}\n\n'
        f'{str(get_paragraphs()[9])}'
    )


@dp.message_handler(commands=['efficiency'])
async def work_process(message: types.Message):
    await message.reply(
        f'{str(get_headers()[10])}\n\n'
        f'{str(get_paragraphs()[10])}'
    )

#1