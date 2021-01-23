from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_tires_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Общие вопросы",
                             callback_data="about_tires")
    ],
    [
        InlineKeyboardButton(text="Технологии маркировки",
                             callback_data="labeling_tires")
    ],
    [
        InlineKeyboardButton(text="Регистрация участника",
                             callback_data="registration_tires")
    ],
    [
        InlineKeyboardButton(text="Описание товара",
                             callback_data="description_tires")
    ],
    [
        InlineKeyboardButton(text="Оплата кодов",
                             callback_data="payment_tires")
    ],
    [
        InlineKeyboardButton(text="Заказ кодов",
                             callback_data="ordering_tires")
    ],
    [
        InlineKeyboardButton(text="Ввод в оборот",
                             callback_data="turnover_tires")
    ],
    [
        InlineKeyboardButton(text="ЭДО",
                             callback_data="ede_tires")
    ],
    [
        InlineKeyboardButton(text="Вывод из оборота",
                             callback_data="withdrawal_tires")
    ],
    [
        InlineKeyboardButton(text="Возврат продукции",
                             callback_data="return_tires")
    ],
    [
        InlineKeyboardButton(text="Перемаркировка",
                             callback_data="remarking_tires")
    ],
    [
        InlineKeyboardButton(text="Агрегирование",
                             callback_data="aggregation_tires")
    ],
    [
        InlineKeyboardButton(text="Документация",
                             callback_data="documentation_tires")
    ],
    [
        InlineKeyboardButton(text="Оптово-розничное звено",
                             callback_data="wholesale_tires")
    ],
    [
        InlineKeyboardButton(text="Импорт",
                             callback_data="import_tires")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_main_questions")
    ],

]
)
