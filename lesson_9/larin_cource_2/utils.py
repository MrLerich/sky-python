import requests
import random
from classes.basic_word import BasicWord

URL_JSON = r'https://jsonkeeper.com/b/Q3A5'


def get_json_from_server(url_json=URL_JSON):
    """Получает json с сервера
    :param url_json
    :return:
    """
    json_db = requests.get(url_json).json()
    return json_db

def load_random_word(url_json=URL_JSON):
    """Получает json с сервера и возвращает экземпляр слова для игры
    :param url_json:
    :return:
    """

    random_word = random.choice(get_json_from_server(url_json))
    basic_word = BasicWord(random_word['word'], random_word['subwords'])

    return basic_word


def put_word_ending(number):
    """
    Делает окончание слова в соответствии с числом перед ним
    :param number:
    :return:
    """
    word_end1 = " слов"
    word_end2 = " слова"
    word_end3 = " слово"
    if number % 100 in [0, 10, 11, 12, 13, 14]:
        return word_end1
    elif number % 10 in [2, 3, 4]:
        return word_end2
    elif number % 10 in [1]:
        return word_end3
    elif number % 10 in [0, 5, 6, 7, 8, 9]:
        return word_end1