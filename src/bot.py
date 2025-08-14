import logging, os
import asyncio
import whisper

from aiogram import Bot, Dispatcher

from config.config import get_config
from handlers.users import router as users_router

async def main():
    conf = get_config()
    
    logging.basicConfig(
        level=conf.log.level,
        format=conf.log.format,
    )

    logger = logging.getLogger(__name__)

    logger.info('Loading whisper model')
    model = whisper.load_model('small')

    bot = Bot(conf.bot.token)
    dp = Dispatcher()

    dp.workflow_data.update(model=model)
    dp.include_router(users_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())