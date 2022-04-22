
import requests

# список вопросов с внешнего ресурса
def load_question():
    """Возвращает вопрос в понятном пользователю виде, например:
         Вопрос: What do people often call American flag? Сложность 4/5"""

    load_questions = requests.get('https://jsonkeeper.com/b/I3W2')
    load_questions_json = load_questions.json()
    return load_questions_json

#статистика
def get_statistics(score_sum,correct_answers):
    """Статистика игры"""
    return f'Вот и всё!\nОтвечено {correct_answers} вопроса из {len(load_question())}.\nНабрано {score_sum} баллов.'

