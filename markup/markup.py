from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from setting.config import LIST_TASK


class Keyboards:
    """
    Класс Keyboards предназначен для создания разметки интерфейса бота
    """
    def __init__(self):
        self.markup = None
        self.DB = None

    def menu_on_start(self):
        """Создает и возвращает стартовую клавиатуру"""
        button_01 = KeyboardButton('/matematica')
        button_02 = KeyboardButton('/Описание')
        button_03 = KeyboardButton('/help')

        self.markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                          one_time_keyboard=True)
        self.markup.add(button_01).add(button_02).add(button_03)

        return self.markup

    def menu_on_pressed_startup(self):
        """Создает и возвращает клавиатуру для команды matematica"""
        button_1 = KeyboardButton('/начать')
        button_2 = KeyboardButton('other')

        self.markup = ReplyKeyboardMarkup(True, True, row_width=3)
        self.markup.add(button_1).insert(button_2)

        return self.markup

    def set_task(self):
        """Создаёт и возвращает клавиатуру для определения вида задания"""
        button_1 = KeyboardButton('/простые_числа')
        button_2 = KeyboardButton('/просто_дроби')

        self.markup = ReplyKeyboardMarkup(True, True)
        self.markup.insert(button_1).insert(button_2)

        return self.markup

    def tasks_inline_kb(self):
        """Создает и возвращает inline клавиатуру: выбор типа задания"""
        self.markup = InlineKeyboardMarkup(row_width=2)
        for names_btn in LIST_TASK:
            button_inline = self.set_inline_btn_str(names_btn)
            # self.markup.add(button_inline)
            self.markup.insert(button_inline)
        return self.markup

    @staticmethod
    def set_inline_btn_str(value: str):
        """
        Создает и возвращает inline-кнопку по входному параметру-строке
        """
        return InlineKeyboardButton(value, callback_data=value)

    @staticmethod
    def remove_menu():
        """
        Удаляет кнопки из меню и возвращает пустое меню
        """
        return ReplyKeyboardRemove()
