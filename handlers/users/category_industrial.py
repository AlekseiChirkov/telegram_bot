from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline.category_industrial_buttons import category_industrial_choice


@dp.callback_query_handler(text='industrial')
async def industrial(call: CallbackQuery):
    await call.message.answer(
        'Маркировка товаров легкой промышленности\n\n'
        'Общие вопросы\n',
        reply_markup=category_industrial_choice,
    )

