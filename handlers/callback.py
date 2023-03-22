from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('question_3', callback_data='button_2')
    markup.add(button_1)
    button_2 = InlineKeyboardButton("question_4", callback_data="button_3")
    markup.add(button_2)
    button_3 = InlineKeyboardButton("question_5", callback_data="button_4")
    markup.add(button_3)
    question = "Какой нынешний месяц обучения?"
    answer = [
        "1",
        "2",
        "3",
        "73",
        "Python",
        "Не знаю",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('question_2', callback_data='button_1')
    markup.add(button_1)
    button_2 = InlineKeyboardButton('question_4', callback_data='button_3')
    markup.add(button_2)
    button_3 = InlineKeyboardButton('question_5', callback_data='button_4')
    markup.add(button_3)
    question = "Как дела?"
    answer = [
        "хорошо",
        "плохо",
        "пойдет",
        "сорок семь",
        "могло быть лучше",
        "не знаю",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('question_2', callback_data='button_1')
    markup.add(button_1)
    button_2 = InlineKeyboardButton('question_3', callback_data='button_2')
    markup.add(button_2)
    button_3 = InlineKeyboardButton('question_5', callback_data='button_4')
    markup.add(button_3)
    question = "Какую максимальную скидку можно получить в GeekTech?"
    answer = [
        "1000",
        "2000",
        "3000",
        "4000",
        "5000",
        "100%",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )

async def quiz_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('question_2', callback_data='button_1')
    markup.add(button_1)
    button_2 = InlineKeyboardButton('question_3', callback_data='button_2')
    markup.add(button_2)
    button_3 = InlineKeyboardButton('question_4', callback_data='button_3')
    markup.add(button_3)
    question = "Сколько всего занятий в месяц?"
    answer = [
        "6",
        "7",
        "9",
        "10",
        "8",
        "5",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        reply_markup=markup
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text='button_2')
    dp.register_callback_query_handler(quiz_4, text='button_3')
    dp.register_callback_query_handler(quiz_5, text='button_4')

