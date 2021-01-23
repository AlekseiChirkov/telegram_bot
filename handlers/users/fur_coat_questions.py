from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.сategory_fur_coat_buttons import category_fur_coat_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text="about_fur_coatq") # message is too long add q in text
async def about_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[13])}\n\n'
        f'{str(get_paragraphs()[13])}',
        reply_markup=category_fur_coat_choice

    )


@dp.callback_query_handler(text="register_fur_coat")
async def register_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[14])}\n\n'
        f'{str(get_paragraphs()[14])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="describe_fur_coat")
async def describe_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[15])}\n\n'
        f'{str(get_paragraphs()[15])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="order_fur_coatq")  # message is too long  add q in text
async def order_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[16])}\n\n'
        f'{str(get_paragraphs()[16])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="label_fur_coat")
async def label_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[17])}\n\n'
        f'{str(get_paragraphs()[17])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="requirements_fur_coat")
async def requirements_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[18])}\n\n'
        f'{str(get_paragraphs()[18])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="import_fur_coatq")  #  Can't parse entities: unsupported start tag "*" at byte offset 1519
async def import_fur_coat(call: CallbackQuery):     # Telegram Bot API currently supports only <b>, <i>, <a>,<code> and <pre> tags, for HTML parse mode
    await call.message.answer(                         # ad q in text
        f'{str(get_headers()[19])}\n\n'
        f'{str(get_paragraphs()[19])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="shipping_fur_coat")
async def shipping_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[20])}\n\n'
        f'{str(get_paragraphs()[20])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="retail_fur_coat")
async def retail_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[21])}\n\n'
        f'{str(get_paragraphs()[21])}',
        reply_markup=category_fur_coat_choice
    )


@dp.callback_query_handler(text="badge_damaged_fur_coat")
async def badge_damaged_fur_coat(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[22])}\n\n'
        f'{str(get_paragraphs()[22])}',
        reply_markup=category_fur_coat_choice
    )
