import functions

def main():
    # данные о студенте
    print('Введите номер студента')
    student_id = int(input())

    student = functions.get_student_by_pk(student_id)

    #если нет студента
    if not student:
        print('У нас нет такого студента')
        quit()

    # Инфа о знаниях и имеющихся студентов
    student_name = student['full_name']
    student_skills = ' '.join(student['skills'])
    student_learn = ' '.join(student['learns'])

    # вывод  инфа о знаниях и имеющихся студентов
    print(f'Студент {student_name}')
    print(f'Знает {student_skills}')

    # смотрим данные о профессии
    print(f'Выберите специальность для оценки студента {student_name}')
    profession_title = input()
    profession = functions.get_profession_by_title(profession_title)

    # если нет профы
    if not profession:
        print('У нас нет такой специальности')
        quit()

    #Смотрим сравнение
    fitness = functions.check_fitness(student, profession)

    #Смотрим данные изи словаря
    fit_percent = fitness['fit_percent']
    has = fitness['has']
    lacks = fitness['lacks']

    #вывод результатов
    print(f'Пригодность {fit_percent}%')
    print(f'{student_name} знает {" ".join(has)}')
    print(f'{student_name} не знает {" ".join(lacks)}')


if __name__=='__main__':
    main()