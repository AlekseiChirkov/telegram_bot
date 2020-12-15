from aiogram import types

from loader import dp


@dp.message_handler(commands=['main'])
async def main_questions(message: types.Message):
    await message.reply(
        'Основные вопросы'
    )