from aiogram import types
from aiogram.utils.markdown import text, bold, italic, code
from aiogram.types import ParseMode, ContentType
from emoji import emojize

from handlers.handler import Handler
from setting.config import HELP_COM_LIST
from setting.messages import *


class HandlerCommands(Handler):
    """
    Класс обрабатывает основные входящие команды (/start, /help)
    """
    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    async def process_start_command(self, message: types.Message):
        await message.reply(START_MESSAGE,
                            reply_markup=self.markup.menu_on_start())

    async def process_help_command(self, message: types.Message):
        msg = text(bold(HELP_PREVIEW), *HELP_COM_LIST, sep='\n')
        await message.reply(msg, parse_mode=ParseMode.MARKDOWN_V2)

    async def process_matematica_command(self, message: types.Message):
        txt = f'{message.from_user.first_name}! {MATICA_SALUTE}'
        # await message.reply(txt)
        await message.answer(txt, reply_markup=self.markup.remove_menu())
        await message.answer(
            'Начать?', reply_markup=self.markup.menu_on_pressed_startup())

    # Команда '/начать'
    async def process_taskstart_command(self, message: types.Message):
        await message.answer(f'{message.from_user.first_name}, выбери занятие',
                             reply_markup=self.markup.remove_menu())
        await self.bot.send_message(
            message.from_user.id,
            text='Уравнение с какими элементами будем решать?',
            reply_markup=self.markup.set_task()
        )

    async def process_fsm_command(self, message: types.Message):
        await message.answer('Inline_choice',
                             reply_markup=self.markup.tasks_inline_kb())

    def handler(self):
        self.dp.register_message_handler(self.process_start_command,
                                         commands=['start'])
        self.dp.register_message_handler(self.process_help_command,
                                         commands=['help'])
        self.dp.register_message_handler(self.process_matematica_command,
                                         commands=['matematica'])
        self.dp.register_message_handler(self.process_fsm_command,
                                         commands=['choice'])
        self.dp.register_message_handler(self.process_taskstart_command,
                                         commands=['начать'])


class HandlerEcho(Handler):
    """
    Класс возвращает неизвестные команды и просто неизвестную информацию
    """
    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    async def echo_message(self, msg: types.Message):
        print('echo')
        await self.bot.send_message(msg.from_user.id, msg.text)

    async def unknown_message(self, msg: types.Message):
        message_text = text(emojize(UNKNOWN), italic('\nЯ просто напомню,'),
                            'что есть', code('команда'), '/help')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN_V2)

    def handler(self):
        # Самая последняя регистрация
        self.dp.register_message_handler(self.echo_message)
        self.dp.register_message_handler(self.unknown_message,
                                         content_types=ContentType.ANY)

    @staticmethod
    def check_is_digit(value):
        if value.isdigit():
            pass
