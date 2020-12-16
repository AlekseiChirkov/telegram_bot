from aiogram import types

from loader import dp

# шубы


@dp.message_handler(commands=['fur_coat'])
async def main_questions(message: types.Message):
    await message.reply(
        'Маркировка шуб\n'
        '/about_marking - О маркировке\n'
        '/how_to_register - Как зарегистрироваться в системе маркировки\n'
        '/how_to_describe - Как описать товары\n'
        '/how_to_order - Как заказать и получить контрольные (идентификационные) знаки (КиЗ, марки)\n'
        '/how_to_label - Как осуществлять маркировку товаров\n'
        '/requirements_for - Требования к RFID-оборудованию и ПО\n'
        '/how_to_import - Как ввезти товар на территорию Российской Федерации не из стран ЕАЭС\n'
        '/shipping - Что делать при отгрузке товаров\n'
        '/retailing - Что делать при розничной продаже товаров\n'
        '/badge_damaged - Что делать, если контрольный (идентификационный) знак испорчен'
    )