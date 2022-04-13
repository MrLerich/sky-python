fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(fish_name):
    for i in fish:
        if i["specie"] == fish_name:
            fishh = fish_name
            water = i["water"]
    return (fishh, water)


# Не удаляйте код ниже, он нужен для проверки!

fish_name = input()
fish, water = get_fish(fish_name)
print(fish, water)
