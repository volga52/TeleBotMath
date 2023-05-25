"""Обработчик машинного состояния"""
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types
from typing import Generator, Optional

from FSM.check_value import CheckValue
from FSM.equation_fsm import FSMEquation
from handlers.handler import Handler
from setting.config import DICT_TASK
from setting.lines import MATICA_PREVIEW, DICT_MES_PREVIEW, \
    CANCEL_MES_PREVIEW, FIRST_EXC_ANSWER, ERROR_CORRECTION, YES, MISPRINT, \
    DENIAL


class HandlerFSM(Handler):
    """Класс обрабатывает машинное состояние """

    def __init__(self, dp):
        self.storage = MemoryStorage()
        super().__init__(dp=dp)
        self.dp.storage = self.storage
        self.inspector = CheckValue()

        self.gen: Optional[Generator] = None
        self.math_cod = None

    async def process_tasks_command(self, message: types.Message,
                                    state: FSMContext):
        """Устанавливает тип уравнений. Запускает FSM состояние"""
        await message.answer('OK', reply_markup=self.markup.remove_menu())
        # Получение ответа с кнопки
        cod = message.text.split('_')[1]
        self.math_cod = DICT_TASK[cod]

        await self.set_state(message, state)

    async def set_state(self, message: types.Message, state: FSMContext):
        """Функция запускает первый этап машинного состояния"""
        text_rules = f"{MATICA_PREVIEW} {DICT_MES_PREVIEW[self.math_cod]}" \
                     f"\n'Набери число и жми ВВОД (ENTER)'" \
                     f"\n{CANCEL_MES_PREVIEW}"
        await self.bot.send_message(message.from_user.id, text_rules)
        await self.bot.send_message(message.from_user.id,
                                    FIRST_EXC_ANSWER[0],
                                    reply_markup=self.markup.remove_menu())
        await FSMEquation.first.set()
        await self.first_state_equation()

    async def math_init(self):
        """Метод запускает создание математических выражений"""
        # Инициация элемента математики
        # *** По окончании требуется очистка
        self.dp.math_element.launch(self.math_cod)
        # Определение количества уравнений
        quantity_tests = self.dp.math_element.quantity_equations
        self.gen = self.generator(quantity_tests)

    async def first_state_equation(self):
        """Обработка первого запроса машинного состояния"""
        await self.math_init()
        # Установка демонстрационного уравнения
        self.dp.math_element.message_dict['equation'] = FIRST_EXC_ANSWER[0]
        self.dp.math_element.message_dict['answer'] = FIRST_EXC_ANSWER[1]
        # print(self.dp.math_element.message_dict)

        await FSMEquation.test.set()

    async def excerpt_state_equation(self, message: types.Message,
                                     state: FSMContext):
        """Вывод фразы-цитаты"""
        if self.dp.math_element.check_ratio_print_ex():
            text = self.dp.math_element.message_dict.get('excerpt', 'None')
            await self.bot.send_message(message.from_user.id, text)
        await FSMEquation.next()
        await self.new_equation(message, state)

    async def test_state_equation(self, message: types.Message,
                                  state: FSMContext):
        """Обработка-работа с уравнениями"""
        await FSMEquation.excerpt.set()
        # Полученный текст сразу проверяем
        response = self.inspector(message.text)  # ->число(хорошо); нет->кортеж
        # ### Реакция на результат

        try:  # Если получили число
            response = int(response)

            if response == self.dp.math_element.message_dict['answer']:
                reply_text = ('Верно', YES)
            else:
                reply_text = ('Не правильно', MISPRINT)

        except ValueError:  # Ответ пользователя не число
            test_dict = {
                MISPRINT: f'Опечатка {ERROR_CORRECTION}',
                DENIAL: 'Не хорошо'}

            reply_text = (test_dict[response], response)
            # print(f'No number: react: {reply_text}')

        await message.reply(reply_text[0])
        message.text = reply_text[1]
        # Стадия 'вывод цитаты'
        # _Корректировка коэффициента вывода цитаты
        self.dp.math_element.count_ratio_correct_answer(reply_text[1])
        # _Переход в другую стадию
        await self.excerpt_state_equation(message, state)

    async def new_equation(self, message: types.Message, state: FSMContext):
        if message.text == YES:
            try:
                gen = next(self.gen)
                await message.reply(f"Test {gen} ", reply=False)
                # Получение нового уравнения
                self.dp.math_element.get_main()
                value_dict = self.dp.math_element.message_dict
                # print(value_dict)
            # Контроль количества уравнений
            except StopIteration:
                await FSMEquation.last.set()
                await self.last_state_equation(message, state)
                return

        equation = self.dp.math_element.message_dict.get('equation', 'None')
        await self.bot.send_message(message.from_user.id, equation)
        await FSMEquation.next()

    async def last_state_equation(self, message: types.Message,
                                  state: FSMContext):
        """Завершение машинного состояния"""
        await message.reply("Last FSM_Finish!!!", reply=False)
        await state.finish()

    async def process_cancel_equation(self, message: types.Message,
                                      state: FSMContext):
        """
        Отмена-выход из машинного состояния через команду или ключевое слово
        """
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Выход из FSM')

    def handler(self):
        self.dp.register_message_handler(
            self.process_tasks_command,
            state='*',
            commands=['простые_числа', 'просто_дроби'])

        self.dp.register_message_handler(self.process_cancel_equation,
                                         state='*', commands=['cancel'])
        self.dp.register_message_handler(self.process_cancel_equation, Text(
            equals=['cancel', 'выход'], ignore_case=True), state='*')
        self.dp.register_message_handler(self.first_state_equation,
                                         state=FSMEquation.first)
        self.dp.register_message_handler(self.excerpt_state_equation,
                                         state=FSMEquation.excerpt)
        self.dp.register_message_handler(self.new_equation,
                                         state=FSMEquation.equation)
        self.dp.register_message_handler(self.test_state_equation,
                                         state=FSMEquation.test)
        self.dp.register_message_handler(self.last_state_equation,
                                         state=FSMEquation.last)

    @staticmethod
    def generator(number: int = 5):
        """Генератор порядкового номера тренировочного уравнения"""
        for i in range(number):
            yield i + 1
