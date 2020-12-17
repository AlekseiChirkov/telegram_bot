from aiogram import types

from loader import dp


@dp.message_handler(commands=['medicine'])
async def medicine(message: types.Message):
    await message.reply(
        'Маркировка лекарств\n\n'
        '/medicine_exp - Об эксперименте\n'
        '/personal_account - Личный кабинет участника: регистрация, авторизация, Усиленная квалифицированная '
        'электронная подпись (УКЭП)\n'
        '/emission_registrars = Регистраторы эмиссии\n'
        '/disposal_registrars Регистраторы выбытия\n'
        '/digital_code = Цифровой код: генерация, нанесение, считывание\n'
        '/equipment = Оборудование\n'
        '/basic_actions = Основные действия участников системы мониторинга движения лекарственных препаратов для '
        'медицинского применения\n'
        '/automation = Автоматизируемые процессы и регистрация сведений в ИС МДЛП\n'
    )
