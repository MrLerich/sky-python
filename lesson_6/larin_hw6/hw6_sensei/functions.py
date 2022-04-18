import random


SPLITTER = '::'


def get_words(filenames):
    with open(filenames, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()

        return words


def shuffle_char_in_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def save_user_result_to_history(user_name, points):
    with open('history.txt', 'a', encoding='utf-8') as f:
        f.write(f'{user_name}{SPLITTER}{points}\n')


def print_statics():
    with open('history.txt', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

        total_count_games = len(data)
        points_list = list()

        for note in data:
            _, points = note.split(SPLITTER)
            points_list.append(points)

        max_record = max(points_list)

        print(f'Всего игр сыграно: {total_count_games}')
        print(f'Максимальный рекорд: {max_record}')
