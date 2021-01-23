from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline.category_tires_buttons import category_tires_choice


@dp.callback_query_handler(text='tires')
async def tires(call: CallbackQuery):
    await call.message.answer(
        'Маркировка шин и покрышек\n\n'
        'Общие вопросы\n'
        'Технологии маркировки\n'
        'Регистрация участника оборота товаров\n'
        'Описание товара\n'
        'Оплата кодов маркировки\n'
        'Заказ кодов маркировки\n'
        'Ввод в оборот\n'
        'ЭДО-Сервис электронного документооборота\n'
        'Вывод из оборота\n'
        'Возврат маркированной продукции\n'
        'Перемаркировка\n'
        'Агрегирование\n'
        'Документация\n'
        'Вопросы оптово-розничного звена\n'
        'Импорт\n'
        'Назад - вернуться назад',
        reply_markup=category_tires_choice
    )
