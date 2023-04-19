from typing import Optional

from setting.messages import MISPRINT, DENIAL

dict_error = {DENIAL: 'Давай все таки порешаем уравнения',
              MISPRINT: 'Ответ должен быть числом'}
tuple_error = (DENIAL, MISPRINT)
TUPLE_OF_NEGATIVES: tuple = ('не', 'no', "don't", "do not")


class CheckValue:
    def __init__(self):
        self.argument: Optional[str] = None
        self.arguments_type = None
        self.list_error = tuple_error
        self.response = False

    def check(self, value):
        self.argument = value
        if self.check_is_digit(value):
            return

        self.checking_for_negation()

    def check_is_digit(self, received: str):
        try:
            self.response = int(received)
            return True
        except ValueError:
            self.response = False
            return False

    def checking_for_negation(self):
        self.response = self.list_error[0 if self.target_is_denial() else 1]
        return

    def target_is_denial(self):
        """Проверка строки на наличие отрицания выполнять упражнение"""
        self.argument.lower()
        answer = False
        for i in TUPLE_OF_NEGATIVES:
            if self.argument.find(i) > -1:
                answer = True
                break
        return answer

    def __call__(self, value):
        self.check(value)
        return self.response


if __name__ == '__main__':
    a = 'a16'
    ab = 'нет не буду'
    c = ['15', a, ab]
    b = CheckValue()
    for i in c:
        print(b(i))
    # print(b(a))
