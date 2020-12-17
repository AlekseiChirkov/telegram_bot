from aiogram import types

from loader import dp


@dp.message_handler(commands=['photo'])
async def photo(message: types.Message):
    await message.reply(
        'Маркировка фотоаппаратов и ламп-вспышек\n'
        '/about_photo - Общие вопросы\n'
        '/photo_exp - Об эксперименте\n'
    )