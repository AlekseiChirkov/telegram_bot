from aiogram import types

from loader import dp


@dp.message_handler(commands=['tobacco'])
async def tobacco(message: types.Message):
    await message.reply(
        'Маркировка табака\n'
        '/about_tobacco - О маркировке\n'
        '/rules_tobacco - Ответственность участников оборота и штрафы\n'
    )