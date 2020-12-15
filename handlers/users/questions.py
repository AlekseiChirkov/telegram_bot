from aiogram import types

from loader import dp


@dp.message_handler(commands=['questions'])
async def questions(message: types.Message):
    await message.reply(
        'Раздел вопросов.\n'
        'Выберите категорию вопроса:\n'
        '/main - основные вопросы.\n'
        '/tobacco - маркировка табака.\n'
        '/fur_coat - маркировка шуб.\n'
        '/shoes - маркировка обуви.\n'
        '/drugs - маркировка лекарств.\n'
        '/photo - маркировка фотоаппаратов и ламп вспышек.\n'
        '/tires - маркировка шин и покрышек.\n'
        '/industrial - маркировка товаров легкой промышленности.\n'
    )
