from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_shoes_buttons import category_shoes_choice
from loader import dp


@dp.callback_query_handler(text='shoes')
async def shoes(call: CallbackQuery):
    await call.message.answer(
        'Маркировка обуви\n\n'
        'Вопросы - общие вопросы\n'
        'Назад - вернуться назад',
        reply_markup=category_shoes_choice,
    )

