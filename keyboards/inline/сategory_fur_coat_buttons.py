from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_fur_coat_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Маркировка", callback_data="about_fur_coat"),

    ],
    [
        InlineKeyboardButton(text="Зарегистрироваться", callback_data="register_fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Описать товары", callback_data="describe_fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Заказать и получить", callback_data="order_fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Как маркировать ?", callback_data="label_fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Требования", callback_data="requirements_fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Как ввезти товар ?", callback_data="import_fur_coat"),
    ],
    [
        InlineKeyboardButton(text="Отгрузка товаров", callback_data="shipping_fur_coat"),

    ],
    [
        InlineKeyboardButton(text="Продажа товаров", callback_data="retail_fur_coat"),

    ],
    [
        InlineKeyboardButton(text="Знак испорчен ?", callback_data="badge_damaged_fur_coat"),
    ],
])
#1