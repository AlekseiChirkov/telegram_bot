from aiogram.types import CallbackQuery

from keyboards.inline.category_tires_buttons import category_tires_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text='about_tires')
async def about_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[35])}\n\n'
        f'{str(get_paragraphs()[34])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='tires_exp')
async def tires_exp(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[36])}\n\n'
        f'{str(get_paragraphs()[35])}',
        reply_markup=category_tires_choice
    )


@dp.message_handler(text='registration_tires')
async def registration_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[37])}\n\n'
        f'{str(get_paragraphs()[36])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='description_tires')
async def description_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[38])}\n\n'
        f'{str(get_paragraphs()[37])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='payment_tires')
async def payment_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[39])}\n\n'
        f'{str(get_paragraphs()[38])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='ordering_tires')
async def ordering_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[40])}\n\n'
        f'{str(get_paragraphs()[39])}',
        reply_markup=category_tires_choice
    )


@dp.message_handler(text='turnover_tires')
async def turnover_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[41])}\n\n'
        f'{str(get_paragraphs()[40])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='ede_tires')
async def ede_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[42])}\n\n'
        f'{str(get_paragraphs()[41])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='withdrawal_tires')
async def withdrawal_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[43])}\n\n'
        f'{str(get_paragraphs()[42])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='return_tires')
async def return_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[45])}\n\n'
        f'{str(get_paragraphs()[44])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='remarking_tires')
async def remarking_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[46])}\n\n'
        f'{str(get_paragraphs()[45])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='aggregation_tires')
async def aggregation_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[47])}\n\n'
        f'{str(get_paragraphs()[46])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='documentation_tires')
async def documentation_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[48])}\n\n'
        f'{str(get_paragraphs()[47])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='wholesale_tires')
async def wholesale_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[49])}\n\n'
        f'{str(get_paragraphs()[48])}',
        reply_markup=category_tires_choice
    )


@dp.callback_query_handler(text='import_tires')
async def import_tires(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[50])}\n\n'
        f'{str(get_paragraphs()[49])}',
        reply_markup=category_tires_choice
    )
