from aiogram import types
from loader import dp

from keyboards.default import start_menu


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        'Добро пожаловать.\n'
        'Здесь вы можете получить ответы на интересующие вас вопросы.\n'
        'Нажмите /help что бы получить подсказку',
        reply_markup=start_menu,
    )



