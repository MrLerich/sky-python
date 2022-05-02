
class Player:

    def __init__(self, name):
        self.name = name
        self.invented_words = []

    # def __repr__(self):
    #     return f'\
    #     \nИмя игрока: {self.name}\
    #     \nПридуманные слова: {self.invented_words}'

    def get_user_name(self):
        """
        Возвращает имя пользователя
        :return:
        """
        return self.name

    def add_correct_words(self, invented_word):
        """
        добавление слова в использованные слова (ничего не возвращает)
        :param invented_word:
        :return:
        """
        self.invented_words.append(invented_word)

    def get_quntity_users_words(self):
        """
        Получение количества слов от игрока (возвращает int)
        :return:
        """
        quntity_users_words = len(self.invented_words)
        return quntity_users_words


    def is_word_in_invented(self, invented_word):
        """
        Возвращает значение True, если придуманное слово есть в наборе 'invented_word'
        ,иначе возвращает значение False
        :param invented_word:
        :return:
        """
        return invented_word in self.invented_words
