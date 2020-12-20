from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

questions_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/main"),
        ],
        [
            KeyboardButton(text="/tobacco"),
        ],
        [
            KeyboardButton(text="/fur_coat"),
        ],
        [
            KeyboardButton(text="/shoes"),
        ],
        [
            KeyboardButton(text="/medicine"),
        ],
        [
            KeyboardButton(text="/photo"),
        ],
        [
            KeyboardButton(text="/tires"),
        ],
        [
            KeyboardButton(text="/industrial"),
        ],
    ],
    resize_keyboard=True,
)
