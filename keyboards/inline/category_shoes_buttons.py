from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_shoes_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Вопросы", callback_data="about_shoes"),

    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_main_questions")
    ],
])
#1