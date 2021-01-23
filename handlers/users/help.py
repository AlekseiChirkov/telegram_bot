from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from keyboards.inline.help_button import help_choice
from loader import dp


@dp.message_handler(Command("start"))
async def help(message: Message):
    await message.answer(
        "Добро пожаловать! Вы можете выбрать следующие разделы:\n"
        "'Вопросы' - выбрать интересующий вас вопрос.\n"
        "'Назад' - вернуться назад",
        reply_markup=help_choice,
    )

