import utils
from classes.player import Player

def main():

    user_name = input("Введите имя игрока\n").strip()

    player = Player(user_name)
    print(f"Привет, {player.get_user_name()}!")

    # выбранный экземпляр класса
    word = utils.load_random_word()
    # слово, из которого придумываем слова
    base_word = word.get_word().upper()
    # количество всех возможных придуманных слов из выбранного
    quntity_subwords = word.get_number_of_subwords()


    print(f"Составьте {quntity_subwords} слов из слова {base_word}\n"
          "Слова должны быть не короче 3 букв\n"
          "Чтобы закончить игру, угадайте все слова или напишите 'стоп'\n"
          "Поехали, ваше первое слово?")

    step_game = 0
    while step_game < quntity_subwords:

        invented_word = input().strip().lower()

        if player.is_word_in_invented(invented_word):
            print(f"Такое слово уже было.")
            continue

        if invented_word == "стоп" or invented_word == "stop":
            print(f"Игра завершена!\nВы угадали {player.get_quntity_users_words} слов")
            quit()

        if word.is_in_subwords(invented_word):          # хорошее - есть в subwords
            player.add_correct_words(invented_word)     #добавляю в список пользовательских хороших слов
            step_game += 1                              # добавляем тк был удачный ход(отгадано слово)
            print(f"Верно\nОсталось угадать {quntity_subwords - player.get_quntity_users_words()} слов")

        else:
            print(f"Неверно\nОсталось угадать {quntity_subwords - player.get_quntity_users_words()} слов")

    print("Cлова закончились, игра завершена!\n"
          f"Вы угадали {player.get_quntity_users_words()} слов")

if __name__ == "__main__":
    main()



