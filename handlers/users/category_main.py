from aiogram import types

from loader import dp


@dp.message_handler(commands=['main'])
async def main_questions(message: types.Message):
    await message.reply(
        'Основные вопросы:\n'
        '/what_for - Зачем нужна система маркировки?\n'
        '/for_whom - Для кого нужна система маркировки?\n'
        '/work_process - Как работает и из чего состоит процесс маркировки?\n'
        '/fake - Что делать, если я нашел подделку?\n'
        '/who_marks - Кто наносит цифровой знак на товар?\n'
        '/make_fake - Почему код нельзя подделать?\n'
        '/who_response - Кто отвечает за работу системы маркировки и прослеживаемости товаров?\n'
        '/what_goods - Какие товары уже сейчас маркируются?\n'
        '/price_growth - Вырастут ли из-за маркировки цены?\n'
        '/efficiency - Эффективна ли система маркировки?\n'
    )
