from aiogram.types import CallbackQuery

from keyboards.inline.help_button import help_choice
from loader import dp


@dp.callback_query_handler(text='help')
async def help(call: CallbackQuery):
    await call.message.answer(
        "Вы можете выбрать следующие разделы:\n"
        "'Вопросы' - выбрать интересующий вас вопрос.\n"
        "'Задать вопрос' - задать свой вопрос.\n"
        "'Назад' - вернуться назад",
        reply_markup=help_choice,
    )

