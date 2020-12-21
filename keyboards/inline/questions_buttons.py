from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

questions_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Основное", callback_data="main"),

    ],
    [
        InlineKeyboardButton(text="Табак", callback_data="tobacco"),
    ],
    [
        InlineKeyboardButton(text="Шуба", callback_data="fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Обувь", callback_data="shoes"),
    ],
    [
        InlineKeyboardButton(text="Лекарство", callback_data="medicine"),
    ],
    [
        InlineKeyboardButton(text="Фото техника", callback_data="photo"),
    ],
    [
        InlineKeyboardButton(text="Шина и покрышка", callback_data="tires"),
    ],
    [
        InlineKeyboardButton(text="Легкая промышленность", callback_data="industrial"),
    ],
])

#1