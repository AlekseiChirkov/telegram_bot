from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.category_medicine_buttons import category_medicine_choice
from loader import dp
from data.question_parser import get_headers, get_paragraphs


@dp.callback_query_handler(text="medicine_exp")
async def medicine_exp(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[25])}\n\n'
        f'{str(get_paragraphs()[24])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="personal_accountq") # message is too long   add in text
async def personal_account(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[26])}\n\n'
        f'{str(get_paragraphs()[25])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="emission_registrarsq")  # message is too long add q in text
async def emission_registrars(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[27])}\n\n'
        f'{str(get_paragraphs()[26])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="disposal_registrarsq") # message is too lond   add q in text
async def disposal_registrars(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[28])}\n\n'
        f'{str(get_paragraphs()[27])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="digital_codeq") #  Message is too long add q
async def digital_code(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[29])}\n\n'
        f'{str(get_paragraphs()[28])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="equipment")
async def equipment(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[30])}\n\n'
        f'{str(get_paragraphs()[29])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="basic_actionsq") # Message is too long  Add q in text
async def basic_actions(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[31])}\n\n'
        f'{str(get_paragraphs()[30])}',
        reply_markup=category_medicine_choice,
    )


@dp.callback_query_handler(text="automationq") # Message is too long Add q in text
async def automation(call: CallbackQuery):
    await call.message.answer(
        f'{str(get_headers()[32])}\n\n'
        f'{str(get_paragraphs()[31])}',
        reply_markup=category_medicine_choice,
    )
