import os

from setting.lines import NUMBER, FRACTION
from setting.setting_core import Settings


'''Системные настройки'''
config = Settings()

# id самого бота, получено экспериментально
BOT_ID = 1573514660

BOT_CONTAINER_NAME = config.bot_container_name
BOT_IMAGE_NAME = config.bot_image_name
BOT_NAME = config.bot_name
BOT_TOKEN = config.bot_token.get_secret_value()
ADMINS = config.admins
USE_REDIS = config.use_redis

DB_USER = config.db_user
PG_PASSWORD = config.pg_password.get_secret_value()
DB_PASS = config.db_pass.get_secret_value()
DB_NAME = config.db_name
DB_HOST = config.db_host

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, DB_NAME)
# print('DB', DATABASE)

'''Настройки для бота'''
# Список команд для help
HELP_COM_LIST: list = ['/test', '/help', '/matematica', '/начать', '/choice']

'''Программные настройки для блока matematica'''
LIST_TASK: tuple = (NUMBER, FRACTION)
DICT_TASK: dict = {'числа': NUMBER, 'дроби': FRACTION}

# Количество уравнений
# NUMBER_SIMPLE_EQUATIONS = 10
NUMBER_SIMPLE_EQUATIONS = 10
NUMBER_CHECK_FRACTIONS = 10

# Значения минимального и максимального чисел в уравнениях для чисел
VALUE_MIN_FOR_SIMPLE_EQUATIONS_START = 10
VALUE_MAX_FOR_SIMPLE_EQUATIONS_START = 20

# Словарь для определения сложности находится в файле fractions_my_math.py
# Уровень сложности для дробей (код от 1 до 10)
DIFFICULTY_LEVEL: str = '1'

# Лозунг - основной афоризм
SLOGAN_APHORISM = 'Математика царица наук'
# Имя файла, содержащего афоризмы. В одной директории с файлом support_soul.py
SOUP_FILE: str = 'soul.txt'

# Список отрицаний
LIST_OF_NEGATIVES: list = ['не', 'Не', 'НЕ', 'no', "don't", 'do not']


if __name__ == '__main__':
    # При импорте файла сразу создастся
    # и провалидируется объект конфига,
    # который можно далее импортировать из разных мест

    for key, value in config:
        print(f'{key}: {value} <{type(value)}>')
