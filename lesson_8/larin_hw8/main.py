
from function import load_question, get_statistics
from classes import Question

print('Игра начинается')

games = len(load_question())

score_sum = 0
correct_answers = 0
for question in load_question():
    s = Question(question['q'], question['d'], question['a'])
    print(s.build_question())
    user_type_answer = input('Введите ответ: ')
    if s.is_correct(user_type_answer):
        correct_answers += 1
        score_sum += s.get_points()
        print(s.build_positive_feedback())
    else:
        print(s.build_negative_feedback())

print(get_statistics(score_sum, correct_answers))
