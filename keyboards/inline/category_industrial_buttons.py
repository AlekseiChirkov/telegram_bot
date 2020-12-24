from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_industrial_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Общие вопросы",
                             callback_data="about_industrial")
    ]
],
)
