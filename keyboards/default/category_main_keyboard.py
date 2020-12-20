from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

category_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/what_for"),
        ],
        [
            KeyboardButton(text="/for_whom"),
        ],
        [
            KeyboardButton(text="/work_process"),
        ],
        [
            KeyboardButton(text="/fake"),
        ],
        [
            KeyboardButton(text="/who_marks"),
        ],
        [
            KeyboardButton(text="/make_fake"),
        ],
        [
            KeyboardButton(text="/who_response"),
        ],
        [
            KeyboardButton(text="/what_goods"),
        ],
        [
            KeyboardButton(text="/price_growth"),
        ],
        [
            KeyboardButton(text="/efficiency "),
        ],
    ],
    resize_keyboard=True,
)
