from aiogram import types

from loader import dp


@dp.message_handler(commands=['industrial'])
async def industrial(message: types.Message):
    await message.reply(
        'Маркировка товаров легкой промышленности\n'
        '/general - Общие вопросы\n'
    )