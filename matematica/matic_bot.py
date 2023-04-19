import logging
from typing import Generator, Optional

from aphorisms.support_soul import Excerpt
# import logs.config.config_log
from matematica.equations_new import MathNumericalEquation
from setting.config import NUMBER, FRACTION
from setting.config import NUMBER_SIMPLE_EQUATIONS, \
    NUMBER_CHECK_FRACTIONS, LIST_OF_NEGATIVES, SLOGAN_APHORISM
from setting.config import VALUE_MAX_FOR_SIMPLE_EQUATIONS_START as VMAX_SE
from setting.config import VALUE_MIN_FOR_SIMPLE_EQUATIONS_START as VMIN_SE
from setting.messages import MISPRINT, DENIAL, YES, MATICBOTELEM_MES_DICT

# *** строки 79, 105
# logger = logging.getLogger('mathic')


class MaticBotElem:
    """Класс оперирует уравнениями"""

    def __init__(self, cod: Optional[str] = None):
        # объект содержащий цитаты
        self.quantity_equations = 10
        self.excerpts = Excerpt()
        # Коэффициент вывода цитаты-афоризма
        self.ratio_correct_answer = 19
        self.ratio_correct_change = 4
        self.username = None
        # объект содержит элементы отображения для Bot-а
        self.message_dict = MATICBOTELEM_MES_DICT
        # экземпляр класса вычисляющего уравнение
        self.game = MathNumericalEquation()
        # Вид уравнений, тип математических элементов
        self.game.cod = cod
        # Изменение уровня сложности.
        # Возвращает сгенерированный список [min, max] значений
        self.gen_level_difficulty: Optional[Generator] = None
        # Генератор создания уравнения. Возвращает сгенерированное уравнение
        self.generator_equations: Optional[Generator] = None

    def launch(self, math_cod: str):
        """Запускает конструктор класса"""
        self.game.cod = math_cod
        self.message_dict['number_test'] = 0
        self.excerpts.string_default = SLOGAN_APHORISM
        self.message_dict['excerpt'] = SLOGAN_APHORISM
        if self.game.cod == NUMBER:
            self.simple_equations()
        if self.game.cod == FRACTION:
            self.gen_level_difficulty = None
            self.generator_equations = None

    def fabric_simple_equations(self):
        """
        Создает и возвращает уравнение 'простые числа'
        :return:
        equation: str уравнение
        right_answer: правильный ответ
        """
        while True:
            # формирование сложности
            interval_values = next(self.gen_level_difficulty)
            self.game.min_ = interval_values[0]
            self.game.max_ = interval_values[1]

            equation: str = self.game.get_equation()
            right_answer: int = self.game.right_answer
            yield equation, right_answer

    def simple_equations(self):
        """
        Функция 'простые уравнения' запускает УЧЁБУ по уравнениям с одним
        неизвестным для целых чисел в выражении вида a+(b+c)=d
        """
        self.quantity_equations = NUMBER_SIMPLE_EQUATIONS
        # Изменение уровня сложности
        # возвращает генератор списка [min, max]
        self.gen_level_difficulty = self.chang_dif_gen_simple_equations()
        # logger.info('Числовые уравнения. Запуск')
        # Создание фабрики уравнений
        self.generator_equations = self.fabric_simple_equations()

    def chang_dif_gen_simple_equations(self):
        """
        Функция генерирует значение интервала чисел в уравнении.
        Возвращает список [min, max]
        """
        # interval_values = [10, 20] :default
        number = self.quantity_equations + 1
        interval_values = [VMIN_SE, VMAX_SE]
        for i in range(number):
            interval_values[0] += 3 * i
            interval_values[1] += 30 * i
            yield interval_values

    def get_main(self):
        """Метод получить 'главное' уравнение и ответ"""
        equation, right_answer = next(self.generator_equations)
        self.message_dict['equation'] = equation
        self.message_dict['answer'] = right_answer

        self.message_dict['number_test'] += 1   # меняем номер уравнения

        str_doc_num_test = f"Уравнение {self.message_dict.get('number_test')}"
        # logger.info(str_doc_num_test)

        return equation

    # Методы участвующие в процессе вывода цитаты
    def count_ratio_correct_answer(self, value, ratio: Optional[int] = None):
        """Увеличение коэффициента в зависимости от правильности ответа"""
        shift = ratio if ratio else self.ratio_correct_change
        modification_dict = {YES: shift,
                             MISPRINT: shift + 6,
                             DENIAL: 21}
        modification = modification_dict.get(value, 21)

        self.ratio_correct_answer += modification

        return self.ratio_correct_answer

    def check_ratio_print_ex(self):
        """Проверка значения коэффициента на 'больше 18'"""
        if value := bool(int(self.ratio_correct_answer / 20)):
            self.ratio_correct_answer = 0
            # Если не нулевое уравнение получаем новую цитату
            if self.message_dict['number_test']:
                self.message_dict['excerpt'] = self.excerpts.get_new_excerpt
        return value


if __name__ == '__main__':
    b = MaticBotElem()
    # a = MaticBotElem('number')
    b.launch(NUMBER)
    print(b.excerpts())
    print(b.message_dict['number_test'])
    for i in range(15):
        print(b.get_main())
    print(b.message_dict['number_test'])
