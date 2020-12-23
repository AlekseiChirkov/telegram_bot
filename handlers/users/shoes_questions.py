from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_shoes_buttons import category_shoes_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text='about_shoesq')  # message is too long add q in text
async def about_shoes(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[23])}\n\n'
        f'{str(get_paragraphs()[23])}',
        reply_markup=category_shoes_choice,
    )
