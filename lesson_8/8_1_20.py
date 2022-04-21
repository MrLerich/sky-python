
class TodoList:
    def __init__(self, tasks = []):
        self.tasks = tasks

    def add_task(self, tasks):
        self.tasks.append(tasks)

# todo_list = ('Купить лампочку', 'Поменять лампочку', 'Выкинуть лампочку')


todo_list = TodoList()
todo_list.add_task('Выключить свет')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Включить свет')

# Не удаляйте этот код, он нужен для проверки

print(" ".join(todo_list.tasks))