import logging
import asyncio

from aiogram import Bot, Dispatcher

from config.config import get_config

async def main():
    conf = get_config()
    
    logging.basicConfig(
        level=conf.log.level,
        format=conf.log.format,
    )

    bot = Bot(conf.bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())