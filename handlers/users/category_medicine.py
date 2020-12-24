from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_medicine_buttons import category_medicine_choice
from loader import dp


@dp.callback_query_handler(text="medicine")
async def medicine(call: CallbackQuery):
    await call.message.answer(
        'Маркировка лекарств\n\n'
        'Эксперимент - об эксперименте\n'
        'Кабинет участника - личный кабинет участника: регистрация, авторизация, Усиленная квалифицированная\n'
        'электронная подпись (УКЭП)\n'
        'Эмиссия - регистраторы эмиссии\n'
        'Выбытие - регистраторы выбытия\n'
        'Цифровой код - цифровой код: генерация, нанесение, считывание\n'
        'Оборудование - оборудование\n'
        'Основные действия - основные действия участников системы мониторинга движения лекарственных препаратов для '
        'медицинского применения\n'
        'АП и РС - Автоматизируемые процессы и регистрация сведений в ИС МДЛП\n',
        reply_markup=category_medicine_choice,
    )
