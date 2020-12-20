from aiogram import types

from loader import dp
from keyboards.default import help_menu


@dp.message_handler(commands=['help'])
async def display_commands(message: types.Message):
    await message.reply(
        'Вы можете ввести следующие команды:\n'
        '/questions - выбрать интересующий вас вопрос.\n'
        '/ask - задать свой вопрос.',
        reply_markup=help_menu
    )
