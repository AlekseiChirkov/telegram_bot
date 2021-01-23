from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_tobacco_buttons import category_tobacco_choice
from loader import dp


@dp.callback_query_handler(text="tobacco")
async def tobacco(call: CallbackQuery):
    await call.message.answer(
        "Маркировка табака\n"
        "'Маркировка ?' - О маркировке\n"
        "'Ответственность ?' - Ответственность участников оборота и штрафы\n"
        "'Назад' - вернуться назад",
        reply_markup=category_tobacco_choice,
    )