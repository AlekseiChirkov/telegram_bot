from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_industrial_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Общие вопросы",
                             callback_data="about_industrial")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_main_questions")
    ],
])
