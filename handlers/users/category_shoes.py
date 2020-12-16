from aiogram import types

from loader import dp


@dp.message_handler(commands=['shoes'])
async def main_questions(message: types.Message):
    await message.reply(
        'Маркировка обуви\n'
        '/general - Общие вопросы\n'
    )
