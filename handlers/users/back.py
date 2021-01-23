from aiogram.types import CallbackQuery

from keyboards.inline.start_button import start_choice
from loader import dp


@dp.callback_query_handler(text="back")
async def back(call: CallbackQuery):
    await call.message.answer(
        "Добро пожаловать.\n"
        "Здесь вы можете получить ответы на интересующие вас вопросы.\n"
        "Нажмите на кнопку 'Помощь', чтобы получить подсказку",
        reply_markup=start_choice)
