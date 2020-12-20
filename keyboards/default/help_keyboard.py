from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/questions"),
        ],
        [
            KeyboardButton(text="/ask")
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True,
)