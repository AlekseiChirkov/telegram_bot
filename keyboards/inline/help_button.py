from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Вопросы", callback_data="questions"),

    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back")
    ],
])
#1