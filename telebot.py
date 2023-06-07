from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from setting.config import BOT_TOKEN, NUMBER
from handlers.handler_main import HandlerMain
# from matematica.matic_bot import MaticBotElem


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
# dp.math_element = MaticBotElem()

handlers = HandlerMain(dp)
handlers.handle()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
