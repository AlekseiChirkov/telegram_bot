from aiogram import types

from loader import dp


@dp.message_handler(commands=['tobacco'])
async def tobacco(message: types.Message):
    await message.reply(
        'Маркировка табака\n'
        '/about_marking - О маркировке\n'
        '/liability_and_fines - Ответственность участников оборота и штрафы\n'
    )