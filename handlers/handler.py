import abc
from aiogram.dispatcher import Dispatcher

from markup.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, dp: Dispatcher = None):
        self.dp = dp
        self.bot = dp.bot
        self.markup = Keyboards()

    @abc.abstractmethod
    async def handler(self):
        pass
