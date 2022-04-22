
class Question:
    """Для вопроса"""

    def __init__(self, q, d, a):
        self.q = q
        self.d = d
        self.a = a

    def is_correct(self, users_answer):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False."""
        if users_answer == self.a:
            return True
        else:
            return False

    def build_question(self):
        return f'Вопрос: {self.q}\nСложность: {self.d}/5\n'

    def get_points(self):
        """Возвращает int, количество баллов.Баллы зависят от сложности:
        за 1 дается 10 баллов, за 5 дается 50 баллов."""
        points = int(self.d) * 10
        return points

    def build_positive_feedback(self):
        """Возвращает :Ответ верный, получено __ баллов"""
        return f'Ответ верный, получено {self.get_points()} баллов'

    def build_negative_feedback(self):
        """Возвращает: Ответ неверный, верный ответ __"""
        return f'Ответ неверный. Верный ответ - {self.a}'

    # def __repr__(self):
    #     return self.q


# def build_feedback(self):
    #     """Возвращает :Ответ верный, получено __ баллов
    #         Возвращает :Ответ неверный, верный ответ __"""
    #
    #     if self.is_correct():
    #         return f'Ответ верный, получено {self.get_points} баллов'
    #     else:
    #         return f'Ответ неверный. Верный ответ - {self.a}'
