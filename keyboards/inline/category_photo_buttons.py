from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_photo_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Общие вопросы",
                             callback_data="about_photo")
    ],
    [
        InlineKeyboardButton(text="Об эксперименте",
                             callback_data="photo_exp")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_main_questions")
    ],
])
