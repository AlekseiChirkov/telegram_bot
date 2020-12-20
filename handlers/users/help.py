from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.help_button import help_choice


@dp.callback_query_handler(text="help")
async def display_commands(call: CallbackQuery):
    await call.message.answer(
        "Вы можете выбрать следующие разделы:\n"
        "'Вопросы' - выбрать интересующий вас вопрос.\n"
        "'Задать вопрос' - задать свой вопрос.",
        reply_markup=help_choice,
    )

