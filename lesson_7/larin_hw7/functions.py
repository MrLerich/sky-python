import json

def load_students():
    '''загружает студентов из файла в список'''
    with open('students.json', 'r', encoding='utf-8') as file:
        record = json.load(file)
    return record


def load_professions():
    '''загружает навыки из файла в список'''
    with open('professions.json', 'r', encoding='utf-8') as file:
        record = json.load(file)
    return record


def get_student_by_pk(pk):
    '''Получает словарь с данными студента по его pk'''
    students = load_students()
    for student in students:
        if student.get('pk') == pk:
            return student
    return None


def get_profession_by_title(title):
    '''Получает словарь с инфо о профе по названию'''
    professions = load_professions()
    for profession in professions:
        if profession.get('title') == title.title():
            return profession
    return None


def check_fitness(student, profession):
    '''получив студента и профессию, возвращала бы словарь определенного типа'''
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(has_skills)

    has_percent = round(len(has_skills)/len(profession_skills)*100)

    has = list(has_skills)
    lacks = list(lacks_skills)

    return {
        'has': has,
        'lacks': lacks,
        'fit_percent': has_percent,
    }


