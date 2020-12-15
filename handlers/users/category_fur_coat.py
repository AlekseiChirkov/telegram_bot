from aiogram import types

from loader import dp

# шубы


@dp.message_handler(commands=['fur_coat'])
async def main_questions(message: types.Message):
    await message.reply(
        'Маркировка шуб\n'
        '/about_marking - О маркировке\n'
    )