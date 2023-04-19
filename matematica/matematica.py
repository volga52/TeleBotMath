"""Первоначальная программа для решения уравнений устным счетом"""
from time import sleep
import logging

# import logs.config.config_log
from setting.config import NUMBER_SIMPLE_EQUATIONS, \
    NUMBER_CHECK_FRACTIONS, LIST_OF_NEGATIVES, SLOGAN_APHORISM
from setting.config import \
    VALUE_MAX_FOR_SIMPLE_EQUATIONS_START as VMAX_SE
from setting.config import \
    VALUE_MIN_FOR_SIMPLE_EQUATIONS_START as VMIN_SE

from matematica.fractions_my_math import GenerationFractions
from matematica.equations_new import MathNumericalEquation
from aphorisms.support_soul import Excerpt
# from aphorisms.support_soul import ExcerptOld as Excerpt

# from telegram_bot.setting.config import BOT_TOKEN


logger = logging.getLogger('mathic')
NUMBER = 'number'
FRACTION = 'fraction'


def simple_equations(quantity=5):
    """
    Функция 'простые уравнения' запускает УЧЁБУ по уравнениям с одним
    неизвестным для целых чисел в выражении вида a+(b+c)=d
    :param quantity: количество уравнений
    """
    logger.info('Числовые уравнения. Запуск')
    game = MathNumericalEquation()
    game.cod = NUMBER
    # Изменение уровня сложности
    # возвращает генератор списка [min, max]
    level_difficulty = changing_dif_gen(quantity)

    for i in range(quantity):
        interval_values = next(level_difficulty)
        print(f'\n*** Уравнение {i + 1}')

        logger.info(f'Уравнение {i + 1}')

        game.min_ = interval_values[0]
        game.max_ = interval_values[1]
        game.run()


def changing_dif_gen(number=5):
    """
    Функция генерирует значение интервала чисел в уравнении.
    Возвращает список [min, max]
    """
    # interval_values = [10, 20] default
    interval_values = [VMIN_SE, VMAX_SE]
    for i in range(number):
        interval_values[0] += 3 * i
        interval_values[1] += 30 * i
        yield interval_values


def check_fractions(number=5):
    """
    Функция запускает УЧЁБУ по уравнениям с одним неизвестным
    для ДРОБЕЙ в выражении вида a+(b+c)=d
    :param number: - количество проходов
    """
    logger.info('Запущен генератор уравнения с дробями')

    game = MathNumericalEquation()
    game.cod = FRACTION

    # Создаем экземпляр класса - генератора дробей
    game.gen_number = GenerationFractions()
    # Меняем уровень сложности
    # Генератор уровня сложности
    level_difficulty = GenerationFractions.start_changing_difficulty_level()

    for i in range(number):
        # Устанавливаем уровень сложности
        game.gen_number.difficulty_level = next(level_difficulty)

        print(f'\n*** Уравнение {i + 1}')
        game.run()


def target_is_denial(string):
    """Проверка строки на наличие отрицания выполнять упражнение"""
    # non_list = ['не', 'no', "don't"]
    string.lower()
    answer = False
    for i in LIST_OF_NEGATIVES:
        if string.find(i) > -1:
            answer = True
            break
    return answer


def fraction_with_integer(number=5):
    pass


def main():
    """Функция запуска программы математического тренажера"""
    excerpts = Excerpt()
    excerpts.string_default = SLOGAN_APHORISM

    user_name = input('Привет! Как тебя зовут? Набери свое имя: ')
    # Вывод первоначального лозунга
    excerpts.print_green_text(excerpts.string_default)

    print('Какие уравнения будем решать?')
    while True:
        answer = input('с числами - введите 1\nс дробями - введите 2'
                       '\nВыход q\nТвое решение? ')
        # Учеба 'уравнения с числами'
        if answer == '1':
            # simple_equations(10)
            simple_equations(NUMBER_SIMPLE_EQUATIONS)
        # Учеба 'уравнения с дробями'
        elif answer == '2':
            check_fractions(NUMBER_CHECK_FRACTIONS)
        # Учеба 'Дроби с целыми числами'
        elif answer == '3':
            pass
        # Выход из программы
        elif answer == 'q':
            print('Пока!')
            sleep(1)
            break
        # Проверка строки на наличие отрицания выполнять упражнение
        elif target_is_denial(answer):
            # выводим афоризм зеленым шрифтом
            excerpts.print_green_text(excerpts())
            sleep(2)
            continue
        else:
            print(f'\n{user_name} Давай все-таки порешаем уравнения\n')
            continue
        print(f'Все решено. {user_name}, ты молодец! \n')
        sleep(2)
        print('Еще будем решать?')


if __name__ == '__main__':
    main()
