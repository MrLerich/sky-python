
class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    # def __repr__(self):
    #     return f'\
    #     \nПервоначальное слово игры: {self.word}\
    #     \nВсе возможные слова: {self.subwords}'

    def get_word(self):
        """Возвращает первоначальное слово для игры"""
        return self.word
    def get_subwords(self):
        """Возвращает все возможные подслова для игры"""
        return self.subwords

    def get_number_of_subwords(self):
        """Возвращает количество возможных вложенных слов"""
        number_of_subwords = len(self.subwords)
        return number_of_subwords

    def is_in_subwords(self, invented_word):
        """Проверяет, есть ли слово, введенное пользователем, в списке вложенных слов
        :param invented_word:
        :return:
        """
        return invented_word in self.subwords