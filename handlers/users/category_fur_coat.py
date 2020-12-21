from aiogram import types

from loader import dp


@dp.message_handler(commands=['fur_coat'])
async def fur_coat(message: types.Message):
    await message.reply(
        'Маркировка шуб\n\n'
        '/about_fur_coat - О маркировке\n'
        '/register_fur_coat - Как зарегистрироваться в системе маркировки\n'
        '/describe_fur_coat - Как описать товары\n'
        '/order_fur_coat - Как заказать и получить контрольные (идентификационные) знаки (КиЗ, марки)\n'
        '/label_fur_coat - Как осуществлять маркировку товаров\n'
        '/requirements_fur_coat - Требования к RFID-оборудованию и ПО\n'
        '/import_fur_coat - Как ввезти товар на территорию Российской Федерации не из стран ЕАЭС\n'
        '/shipping_fur_coat - Что делать при отгрузке товаров\n'
        '/retail_fur_coat - Что делать при розничной продаже товаров\n'
        '/badge_damaged_fur_coat - Что делать, если контрольный (идентификационный) знак испорчен\n'
    )

