from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.сategory_fur_coat_buttons import category_fur_coat_choice
from loader import dp


@dp.callback_query_handler(text="fur_coat")
async def fur_coat(call: CallbackQuery):
    await call.message.answer(
        'Маркировка шуб\n\n'
        'Маркировка - О маркировке\n'
        'Зарегистрироваться - Как зарегистрироваться в системе маркировки\n'
        'Описать товары - Как описать товары\n'
        'Заказать и получить - Как заказать и получить контрольные (идентификационные) знаки (КиЗ, марки)\n'
        'Как маркировать ? - Как осуществлять маркировку товаров\n'
        'Требования - Требования к RFID-оборудованию и ПО\n'
        'Как ввезти товар ? - Как ввезти товар на территорию Российской Федерации не из стран ЕАЭС\n'
        'Отгрузка товаров - Что делать при отгрузке товаров\n'
        'Продажа товаров - Что делать при розничной продаже товаров\n'
        'Знак испорчен ? - Что делать, если контрольный (идентификационный) знак испорчен\n',
        reply_markup=category_fur_coat_choice,
    )

