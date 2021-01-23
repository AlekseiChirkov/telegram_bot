from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_medicine_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Эксперимент", callback_data="medicine_exp"),

    ],
    [
        InlineKeyboardButton(text="Кабинет участника", callback_data="personal_account"),
    ],
    [
        InlineKeyboardButton(text="Эмиссия", callback_data="emission_registrars"),
    ],
    [
        InlineKeyboardButton(text="Выбытие", callback_data="disposal_registrars"),
    ],
    [
        InlineKeyboardButton(text="Цифровой код", callback_data="digital_code"),
    ],
    [
        InlineKeyboardButton(text="Оборудование", callback_data="equipment"),
    ],
    [
        InlineKeyboardButton(text="Основные действия", callback_data="basic_actions"),

    ],
    [
        InlineKeyboardButton(text="АП и РС", callback_data="automation"),
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_main_questions")
    ],
])
#1