import logging.handlers
from pathlib import Path
import sys


LOGGING_LEVEL = 'DEBUG'

PATH = Path(__file__).resolve().parent.parent
PATH = f'{PATH}/files/math.log'

LOG_MATH = logging.getLogger('mathic')
FORMATTER_FOR_MATH = logging.Formatter('%(asctime)-27s %(levelname)-10s %(filename)-23s %(message)s')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)

STREAM_HANDLER.setFormatter(FORMATTER_FOR_MATH)
STREAM_HANDLER.setLevel(logging.ERROR)

NAME_LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='midnight')
NAME_LOG_FILE.setFormatter(FORMATTER_FOR_MATH)

LOG_MATH.addHandler(STREAM_HANDLER)
LOG_MATH.addHandler(NAME_LOG_FILE)
LOG_MATH.setLevel(LOGGING_LEVEL)

if __name__ == '__name__':
    LOG_MATH.critical('Критическая ошибка')
    LOG_MATH.error('Ошибка')
    LOG_MATH.debug('Отладочная информация')
    LOG_MATH.info('Информационное сообщение')
