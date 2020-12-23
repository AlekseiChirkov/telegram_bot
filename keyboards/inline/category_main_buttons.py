from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_main_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зачем ?", callback_data="what_for"),

    ],
    [
        InlineKeyboardButton(text="Для кого ?", callback_data="for_whom"),
    ],
    [
        InlineKeyboardButton(text="Как это работает ?", callback_data="work_process"),
    ],
    [
        InlineKeyboardButton(text="Фейк ?", callback_data="fake"),
    ],
    [
        InlineKeyboardButton(text="Кто наносит ?", callback_data="who_marks"),
    ],
    [
        InlineKeyboardButton(text="Нельзя подделать ?", callback_data="make_fake"),
    ],
    [
        InlineKeyboardButton(text="Кто отвечает ?", callback_data="who_response"),
    ],
    [
        InlineKeyboardButton(text="Какие товары ?", callback_data="what_goods"),

    ],
    [
        InlineKeyboardButton(text="ЦРПТ ?", callback_data="CRPT"),

    ],
    [
        InlineKeyboardButton(text="Рост цен ?", callback_data="price_growth"),
    ],
    [
        InlineKeyboardButton(text="Эффективна ?", callback_data="efficiency"),
    ],
])
#1