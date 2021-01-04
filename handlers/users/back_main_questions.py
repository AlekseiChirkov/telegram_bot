from aiogram.types import CallbackQuery

from keyboards.inline.questions_buttons import questions_choice
from loader import dp


@dp.callback_query_handler(text="back_main_questions")
async def back_main_questions(call: CallbackQuery):
    await call.message.answer(
        "Раздел вопросов.\n"
        "Выберите категорию вопроса:\n"
        "'Основное' - основные вопросы.\n"
        "'Табак' - маркировка табака.\n"
        "'Шуба' - маркировка шуб.\n"
        "'Обувь' - маркировка обуви.\n"
        "'Лекарство' - маркировка лекарств.\n"
        "'Фото техника' - маркировка фотоаппаратов и ламп вспышек.\n"
        "'Шина и покрышка' - маркировка шин и покрышек.\n"
        "'Легкая ' - маркировка товаров легкой промышленности.\n"
        "'Назад' - вернуться назад",
        reply_markup=questions_choice,
    )
