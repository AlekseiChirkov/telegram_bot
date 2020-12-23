from aiogram.types import CallbackQuery
from loader import dp

from keyboards.inline.category_industrial_buttons import category_industrial_choice
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text='about_industrial')
async def about_industrial(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[52])}\n\n'
        f'{str(get_paragraphs()[51])}',
        reply_markup=category_industrial_choice,
    )
