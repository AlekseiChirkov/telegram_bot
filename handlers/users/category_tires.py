from aiogram import types

from loader import dp


@dp.message_handler(commands=['tires'])
async def tires(message: types.Message):
    await message.reply(
        'Маркировка шин и покрышек\n'
        '/about_tires - Общие вопросы\n'
        '/labeling_tires - Технологии маркировки\n'
        '/registration_tires - Регистрация участника оборота товаров\n'
        '/description_tires - Описание товара\n'
        '/payment_tires - Оплата кодов маркировки\n'
        '/ordering_tires - Заказ кодов маркировки\n'
        '/turnover_tires - Ввод в оборот\n'
        '/ede_tires - ЭДО\n'
        '/withdrawal_tires - Вывод товара из оборота\n'
        '/return_tires - Возврат маркированной продукции\n'
        '/remarking_tires - Перемаркировка\n'
        '/aggregation_tires - Агрегирование\n'
        '/documentation_tires - Документация\n'
        '/wholesale_tires - Вопросы оптово-розничного звена\n'
        '/import_tires - Импорт\n'
    )
