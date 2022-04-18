class Hero:

  def __init__(self, name, things=[]):
    self.name = name
    self.things = things

  def collect(self, things):
    self.things.append(things)

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир")
pythomir.collect("Усы хитрости")
pythomir.collect("Рукавички пряморукости")

if len(pythomir.things) == 2:
  print("Проверка пройдена")
else:
  print("Добавление в список things работает некорректно")