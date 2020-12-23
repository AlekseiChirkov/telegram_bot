from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_shoes_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Вопросы", callback_data="about_shoes"),

    ],
])
#1