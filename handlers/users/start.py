from aiogram import types

from loader import dp


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        'Добропожаловать.\n'
        'Здесь вы можете получить ответы на интересующие вас вопросы.\n'
        'Введите /help что бы получить подсказку'
    )