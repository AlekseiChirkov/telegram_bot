from aiogram import types

from loader import dp


@dp.message_handler(commands=['medicine'])
async def main_questions(message: types.Message):
    await message.reply(
        """
        Маркировка лекарств
        /experiments - Об эксперименте
        /personal - Личный кабинет участника: регистрация, авторизация, Усиленная квалифицированная электронная подпись (УКЭП)
        /emission_registrars = Регистраторы эмиссии
        /disposal_registrars Регистраторы выбытия
        /digital_code = Цифровой код: генерация, нанесение, считывание
        /equipment = Оборудование
        /basic_actions = Основные действия участников системы мониторинга движения лекарственных препаратов для медицинского применения
        /automation = Автоматизируемые процессы и регистрация сведений в ИС МДЛП
        """
    )
