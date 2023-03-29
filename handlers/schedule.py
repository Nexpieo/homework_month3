from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from config import bot, ADMINS


async def birthday(bot: Bot):
    await bot.send_message(ADMINS[0], "Happy Birthday")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(
        birthday,
        trigger=CronTrigger(
            month=5,
            day=10
        ),
        kwargs={"bot": bot},
    )
    scheduler.start()
