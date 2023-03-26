from aiogram.utils import executor
from config import dp
from handlers import callback, client, extra, admin, fsmAdminMentor
from database.bot_db import sql_create
import logging


async def table_create(_):
    sql_create()

fsmAdminMentor.register_handlers_fsm(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=table_create)
