from math import floor
from random import randint
from fractions import Fraction

from setting.config import DIFFICULTY_LEVEL


class GenerationFractions:
    """
    Класс генерирует дроби
    """

    def __init__(self, difficulty_level=DIFFICULTY_LEVEL):
        self.a = None
        self.b = None
        self.d = None
        self.c = None
        self.difficulty_level = difficulty_level
        self.basis = None

        self.min_ = None
        self.max_ = None
        self.basis_level = None
        # Инициализация аргументов min, max, basis_level
        self.init()

    def generation_fraction(self):
        """
        Функция генерирует 3 дроби и распределяет их по атрибутам класса
        """
        # Генерируем знаменатель дроби
        self.basis = randint(self.min_, self.max_)
        # Используем тип данных 'множество'. Значения не будут повторяться.
        kit = set()
        # Счетчик циклов
        count_while = 0
        # Нужны 3 значения
        while len(kit) != 3:
            # Если значения зацикливаются, все данные обновляем
            if count_while == 6:
                # Генерируем знаменатель дроби
                self.basis = randint(self.min_, self.max_)
                kit = set()
                count_while = 0
            count_while += 1
            # print(f'While {kit}')
            # Числитель будет не больше знаменателя
            next_number = randint(self.min_, self.get_basis())
            kit.add(next_number)

        self.a = Fraction(kit.pop(), self.get_basis())
        self.b = Fraction(kit.pop(), self.get_basis())
        self.d = Fraction(kit.pop(), self.get_basis())

    def get_basis(self):
        """
        Функция возвращает числитель дроби в зависимости от basis_level
        'one' - один числитель на все дроби
        'many' - все дроби имеют разные числители
        """
        if self.basis_level == 'one':
            return self.basis
        elif self.basis_level == 'many':
            return randint(self.min_, self.max_)

    def init(self):
        """
        Функция инициализирует min, max, basis_level настоящего класса
        по полученному коду
        """
        difficulty_dict = {
            '1': [3, 25, 'one'],
            '2': [4, 50, 'one'],
            '3': [3, 9, 'many'],
            '4': [4, 50, 'many'],
            '5': [180, 300, 'many'],
        }
        self.min_, self.max_, self.basis_level = \
            difficulty_dict[self.difficulty_level]

    @staticmethod
    def start_changing_difficulty_level(number=10):
        """
        Функция изменяет уровень сложности
        :param number: количество проходов
        :return: str значение из списка ['1', '2', '3', '4', '5', '6']
        """
        diff_level = '1'
        for i in range(number):
            # после каждого четвертого уравнения поднимаем уровень на 1
            diff_level = ['1', '2', '3', '4', '5', '6'][floor(i/4)]
            yield diff_level

    @staticmethod
    def crush(fraction):
        """
        Функция разделяет числитель и знаменатель дроби
        возвращает их списком
        В последней версии не используется
        """
        str_fraction = str(fraction)
        # Другой способ, возвращает кортеж (числитель, знаменатель)
        other = fraction.as_integer_ratio()

        return [int(number) for number in str_fraction.split('/')]


if __name__ == '__main__':
    pass
    # from time import sleep
    #
    # for i in range(50):
    #     check = GenerationFractions()
    #     check.generation_fraction()
    #     print(check.a, check.d, check.b)
    #     sleep(0.5)

    # a = Fraction(45, 7)
    # print(a.as_integer_ratio())
    # b = '  45/7 '
    # print(Fraction(b))
