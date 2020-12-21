from aiogram import types

from loader import dp


@dp.message_handler(commands=['shoes'])
async def shoes(message: types.Message):
    await message.reply(
        'Маркировка обуви\n\n'
        '/about_shoes - Общие вопросы\n'
    )

