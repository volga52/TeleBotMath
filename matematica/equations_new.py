import logging
from random import randint
from typing import Optional

import logs.config.config_log
from setting.config import NUMBER, FRACTION

# *** строки 74, 95
logger = logging.getLogger('mathic')


class MathNumericalEquation:
    """Класс создания уравнений. Их проверки"""

    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.sign_first = ''
        self.sign_second = ''
        self.right_answer: Optional[int] = None
        self.min_ = 10
        self.max_ = 20
        # self.cod = None
        self.cod = NUMBER
        # Генератор элементов уравнения
        self.gen_number = None

    def set_values(self, cod):
        """
        Метод устанавливает значения 'a', 'b', 'c'
        для выражения вида a+(b+c)=d
        """
        self.cod = cod
        if self.cod == NUMBER:
            self.a = self.generation_number()
            self.b = self.generation_number()
            self.d = self.generation_number()
        if self.cod == FRACTION:
            # Для дробей используем генератор дробей
            gen_numbers = self.gen_number
            gen_numbers.generation_fraction()
            self.a = gen_numbers.a
            self.b = gen_numbers.b
            self.d = gen_numbers.d

    def get_values(self):
        """
        Функция случайно расставляет математические знаки, вычисляет
        значение c по известным a, b, d. для выражения вида a+(b+c)=d.
        """
        # Список математических знаков
        list_operations = ['+', '-']

        if self.d - self.a > 0:
            self.sign_first = list_operations[0]
            if self.b < self.d - self.a:
                self.c = self.d - self.a - self.b
                self.sign_second = list_operations[0]
            else:
                self.c = self.b - self.d + self.a
                self.sign_second = list_operations[1]

        else:
            self.sign_first = list_operations[1]
            if self.b < self.a - self.d:
                self.c = self.a - self.d - self.b
                self.sign_second = list_operations[0]
            else:
                self.c = self.b - self.a + self.d
                self.sign_second = list_operations[1]

        # logger.info(f'Элементы выражения {self.a} {self.b} {self.c} {self.d}')

    def create_rebus(self):
        """
        Функция составляет учебное уравнение и возвращает его в виде строки
        Одно из чисел скрывается, случайным образом.
        Его значение записывается в атрибут 'right_answer'
        """
        # Список слагаемых для выражения a + (b + c) = d
        terms_list = [self.d, self.a, self.b, self.c]
        # Случайный выбор 'неизвестного' из a, b, c
        # unknown_position = random.randint(1, 3)
        unknown_position = randint(1, 3)
        # Сохраняем правильный ответ
        self.right_answer = terms_list[unknown_position]
        # Заменяем значение 'неизвестного' на 'х'
        terms_list[unknown_position] = 'x'

        # Создаём строку учебного уравнения
        equation_string = self.create_string(terms_list)

        # logger.info(f"Составлено уравнение '{equation_string}' "
        #             f'Ответ {self.right_answer}')
        return equation_string

    def create_string(self, list_param=None):
        """
        Функция составляет строку отображения уравнения вида a+(b+c)=d
        Принимает список элементов выражения [d, a, b, c]
        если списка нет подставляет элементы экземпляра класса
        """
        if not list_param:
            terms_list = [self.d, self.a, self.b, self.c]
        else:
            terms_list = list_param

        if isinstance(terms_list[3], int):
            # Если 'с' число требуется его абсолютное значение, т.к.
            # знаки арифметических действий определяются функцией 'get_values'
            terms_list[3] = abs(self.c)

        test_string = f'{terms_list[1]} {self.sign_first} ' \
                      f'({terms_list[2]} {self.sign_second} {terms_list[3]})' \
                      f' = {terms_list[0]}'
        return test_string

    def generation_number(self):
        """
        Функция генерирует случайное целое число в диапазоне i_min : i_max
        """
        return randint(self.min_, self.max_)

    def get_equation(self):
        """Функция выдает уравнение"""
        # Создаем выражение a+(b+c)=d
        self.set_values(self.cod)
        # Заполняем элементами
        self.get_values()
        # Составляем уравнение
        finish_string = self.create_rebus()

        return finish_string


if __name__ == '__main__':
    a = MathNumericalEquation()
    print(a.get_equation)
