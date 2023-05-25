"""Файл содержит стандартные сообщения"""
NUMBER = 'number'
FRACTION = 'fraction'

'''Bot - элементы'''
START_MESSAGE = "Привет!\nНапиши мне что нибудь\nИспользуй /help, чтобы " \
                "узнать список доступных команд! "

HELP_PREVIEW = 'Я могу ответить на следующие команды:'

UNKNOWN = 'Я не знаю, что с этим делать :astonished:'

MATICA_SALUTE = 'Matematica приветствует Тебя '
MATICA_PREVIEW = f"Чтобы ответить, чему равен 'x' вводи только"

'''Математические элементы'''
YES = 'Yes'
MISPRINT = 'misprint'
DENIAL = 'denial'
ERROR_CORRECTION = 'Ответ должен быть числом'
# RIGHT = 'Верно'

number_mes_preview = f"цифры"
fraction_mes_preview = f"дробь.\nДробь вводится через знак /. Например '5/6'"
CANCEL_MES_PREVIEW = f"Чтобы выйти 'cancel' или '/cancel'"

DICT_MES_PREVIEW = {NUMBER: number_mes_preview, FRACTION: fraction_mes_preview}

# Словарь содержит элементы отображения в Bot-е
MATICBOTELEM_MES_DICT = {'number_test': 0,
                         'equation': None,
                         'excerpt': None,
                         'answer': None}

# Первое уравнение с ответом
FIRST_EXC_ANSWER: tuple = ('1 + x = 2', 1)
