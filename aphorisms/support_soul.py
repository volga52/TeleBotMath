from random import shuffle
from pathlib import Path

from setting.config import SOUP_FILE, SLOGAN_APHORISM


class Excerpt:
    """
    Класс содержит и возвращает строки из файла (по умолчанию файл 'soul.txt')
    В дополнение, содержит функции вывода цветного шрифта
    """

    def __init__(self, file_name=SOUP_FILE):
        self.file_name = file_name
        self.excerpts = self.get_excerpt()
        self.string_default = 'Новое\n'

    def __call__(self, *args, **kwargs):
        return self.get_new_excerpt

    @property
    def get_text(self):
        """Возвращает список строк файла"""
        path = Path(__file__).resolve().parent
        try:
            with open(f'{path}/{SOUP_FILE}', 'r', encoding='utf-8') \
                    as file_text:
                text_list = [line for line in file_text]
                shuffle(text_list)
        except FileNotFoundError:
            text_list = [SLOGAN_APHORISM for i in range(10)]
        return text_list

    @property
    def get_new_excerpt(self):
        """Возвращает одну строку из файла"""
        try:
            returned_string = next(self.excerpts)
        # Если афоризмы закончились перезапускаем класс
        except StopIteration:
            self.__init__()
            returned_string = self.string_default
        return returned_string

    def get_excerpt(self):
        """Функция организует поток строк."""
        for string in self.get_text:
            yield string


if __name__ == '__main__':
    a = Excerpt()
    for i in range(55):
        print(a())
