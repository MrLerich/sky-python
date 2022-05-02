import utils
from utils import load_random_word
from classes.player import Player
from classes.basic_word import BasicWord


def main():

    user_name = input("Введите имя игрока\n").strip()

    player = Player(user_name)
    print(f"Привет, {player.get_user_name()}!")

    # выбранный экземпляр класса
    word = utils.load_random_word()
    # слово, из которого придумываем слова
    base_word = word.get_word().upper()
    # print(base_word)
    # количество всех возможных придуманных слов из выбранного
    quntity_subwords = word.get_number_of_subwords()
    # print(quntity_subwords)

    print(f"Составьте {quntity_subwords} слов из слова {base_word}\n"
          "Слова должны быть не короче 3 букв\n"
          "Чтобы закончить игру, угадайте все слова или напишите 'стоп'\n"
          "Поехали, ваше первое слово?")

    step_game = 0
    while step_game < quntity_subwords:

        invented_word = input().strip().lower()

        if invented_word == "стоп" or invented_word == "stop":
            print(f"Игра завершена!\nВы угадали {player.get_quntity_users_words} слов")

        if word.is_in_subwords(invented_word): # хорошее - есть в subwords
            player.add_correct_words(invented_word)     #добавляю в список пльзовательских хороших слов
            step_game = quntity_subwords - player.get_quntity_users_words() # вычисляю осталось ходов
            print(f"Верно\nОсталось угадать {step_game} слов")
            continue
        # elif player.is_word_in_invented(invented_word): #ХОЧУ ЗАПИСАТЬ ЕСЛИ ПРИДУМАННОЕ СЛОВО УЖЕ БЫЛО В УГАДАННЫХ,ТО ИДТИ ДАЛЬШЕ УГАДЫВАТЬ НЕ ИЗМЕНЯЯ СЧЕТЧИКИ
        #     step_game = quntity_subwords - player.get_quntity_users_words()  # вычисляю осталось ходов
        #     print(f"Верно, но вы уже отгадали это слово\nОсталось угадать {step_game} слов")

        # if invented_word НЕТ В SUBWORDS:
        #     print(f"Неверно\nОсталось угадать {step_game} слов")
        #



    print("Cлова закончились, игра завершена!\n"
          f"Вы угадали {len(player.get_quntity_users_words())} слов")


if __name__ == "__main__":
    main()



