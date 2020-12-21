from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.inline.start_button import start_choice
from loader import dp


@dp.message_handler(Command("start"))
async def send_welcome(message: Message):
    await message.answer(text="Добро пожаловать.\n"
                              "Здесь вы можете получить ответы на интересующие вас вопросы.\n"
                              "Нажмите на кнопку 'Помощь', чтобы получить подсказку",
                         reply_markup=start_choice,)

#1