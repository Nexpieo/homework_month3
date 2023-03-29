from aiogram import Dispatcher, types
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from parser.products import get_data_from_page


async def start_command(message: types.Message):
    await message.answer_photo(types.InputFile(r"C:\Users\Admin\Downloads\200px-Wojak.png"))


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("question_2", callback_data="button_1")
    markup.add(button_1)
    button_2 = InlineKeyboardButton("question_3", callback_data="button_2")
    markup.add(button_2)
    button_3 = InlineKeyboardButton("question_4", callback_data="button_3")
    markup.add(button_3)
    button_4 = InlineKeyboardButton('question_5', callback_data='button_4')
    markup.add(button_4)


    question = "Как зовут учителя?"
    answer = [
        "Владимир",
        "Боб",
        "Эсенбек",
        "Гриффит",
        "Дио",
        "Карл",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )


async def get_products(message: types.Message):
    products = get_data_from_page()
    for product in products:
        await message.answer(
            f"{product['link']}\n"
            f"{product['title']}\n"
            f"{product['price']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(get_products, commands=['get'])