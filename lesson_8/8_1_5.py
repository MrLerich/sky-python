class Hero:

  def go_right(self, dist):
    print(f"Я иду {dist} метров направо")

  def go_left(self, dist):
    print(f"Я иду {dist} метров налево")

  def observe(self):
    print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()

