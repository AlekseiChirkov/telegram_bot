from aiogram import types

from loader import dp


@dp.message_handler(commands=['tires'])
async def tires(message: types.Message):
    await message.reply(
        'Маркировка фотоаппаратов и ламп-вспышек\n'
        '/general_issues - Общие вопросы\n'
        '/marking - Об эксперименте\n'
        '/registration - Регистрация участника оборота товаров\n'
        '/description - Описание товара\n'
        '/payment - Оплата кодов маркировки\n'
        '/ordering - Заказ кодов маркировки\n'
        '/putting - Ввод в оборот\n'
        '/edf - ЭДО\n'
        '/withdrawal - Вывод товара из оборота\n'
        '/return_product - Возврат маркированной продукции\n'
        '/remarking - Перемаркировка\n'
        '/aggregation - Агрегирование\n'
        '/documentation - Документация\n'
        '/wholesale - Вопросы оптово-розничного звена\n'
        '/importation - Импорт\n'
    )