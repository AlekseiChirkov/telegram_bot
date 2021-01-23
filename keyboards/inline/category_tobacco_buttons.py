from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_tobacco_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Маркировка ?", callback_data="about_tobacco"),

    ],
    [
        InlineKeyboardButton(text="Ответственность ?", callback_data="rules_tobacco"),
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_main_questions")
    ],
])
#1