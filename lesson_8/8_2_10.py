class Hero():

    def __init__(self, name, posessions):
        self.name = name
        self.posessions = posessions

    def __repr__(self):
        #posessions = self.posessions
        #a = ', '.join(self.posessions)  #print(*posessions, sep=',')
        return (f'Герой {self.name} взял с собой {", ".join(self.posessions)}')

hero = Hero("Питомир", ["меч", "плащ", "шляпа"])

print(hero)