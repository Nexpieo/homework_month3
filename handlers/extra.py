import random

from aiogram import Dispatcher, types
from config import ADMINS
from random import choice


async def echo(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)

    if message.chat.type != "private":
        if message.from_user.id in ADMINS:
            if message.text.startswith('game'):
                dice = ['🎲', '🎯', '🏀', '⚽', '🎳', '🎰']
                await message.answer_dice(emoji=random.choice(dice))


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
