from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.category_photo_buttons import category_photo_choice


@dp.callback_query_handler(text='photo')
async def photo(call: CallbackQuery):
    await call.message.answer(
        'Маркировка фотоаппаратов и ламп-вспышек\n\n'
        'Общие вопросы\n'
        'Об эксперименте\n',
        reply_markup=category_photo_choice
    )
