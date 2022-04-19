#Задача 4
class Bottle:

    def __init__(self, color, content=0.0):
        self.color = color
        self.content = content

    def get_content(self):
        return int(self.content)

    def fill(self, volume):
        self.content += volume
        return self.content

bottle_1 = Bottle('Красная')
bottle_2 = Bottle('Синяя')

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())