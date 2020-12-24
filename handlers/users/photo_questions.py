from aiogram.types import CallbackQuery
from loader import dp

from data.question_parser import get_headers, get_paragraphs
from keyboards.inline.category_photo_buttons import category_photo_choice


@dp.callback_query_handler(text='about_photo')
async def about_photo(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[33])}\n\n'
        f'{str(get_paragraphs()[32])}',
        reply_markup=category_photo_choice
    )


@dp.message_handler(text='photo_exp')
async def photo_exp(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[34])}\n\n'
        f'{str(get_paragraphs()[33])}',
        reply_markup=category_photo_choice
    )
