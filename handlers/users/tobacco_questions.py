from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_tobacco_buttons import category_tobacco_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text="about_tobaccoq")  #Message is too long, true text="about_tobacco"
async def about_tobacco(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[11])}\n'
        f'{str(get_paragraphs()[11])}',
        reply_markup=category_tobacco_choice,
    )


@dp.callback_query_handler(text="rules_tobacco")
async def rules_tobacco(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[12])}\n\n'
        f'{str(get_paragraphs()[12])}',
        reply_markup=category_tobacco_choice,
    )

