from aiogram import types, Dispatcher
from config import ADMINS, bot


async def pin(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id in ADMINS:
            if not message.reply_to_message:
                await message.answer("Команда должна быть ответом на сообщение!")
            else:
                await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
