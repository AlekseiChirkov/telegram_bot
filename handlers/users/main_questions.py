from aiogram.types import CallbackQuery

from keyboards.inline.category_main_buttons import category_main_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text="what_for")
async def what_for(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[0])}\n\n'
        f'{str(get_paragraphs()[0])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="for_whom")
async def for_whom(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[1])}\n\n'
        f'{str(get_paragraphs()[1])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="work_process")
async def work_process(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[2])}\n\n'
        f'{str(get_paragraphs()[2])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="fake")
async def fake(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[3])}\n\n'
        f'{str(get_paragraphs()[3])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="who_marks")
async def who_marks(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[4])}\n\n'
        f'{str(get_paragraphs()[4])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="make_fake")
async def make_fake(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[5])}\n\n'
        f'{str(get_paragraphs()[5])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="who_response")
async def who_response(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[6])}\n\n'
        f'{str(get_paragraphs()[6])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="what_goods")
async def what_goods(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[7])}\n\n'
        f'{str(get_paragraphs()[7])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="CRPT")
async def crpt(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[8])}\n\n'
        f'{str(get_paragraphs()[8])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="price_growth")
async def price_growth(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[9])}\n\n'
        f'{str(get_paragraphs()[9])}',
        reply_markup=category_main_choice,
    )


@dp.callback_query_handler(text="efficiency")
async def efficiency(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[10])}\n\n'
        f'{str(get_paragraphs()[10])}',
        reply_markup=category_main_choice,
    )

#1