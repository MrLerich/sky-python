order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []
#в видео 7.2.3
for i in order:
    fish = {
        "count": int(i["skolko"]),
        "specie": i["poroda"].capitalize(),
        "avg_size": int(i["sred_razmer"]/10)
    }
    order_converted.append(fish)

#print(order_converted)
# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)

'''Формат заказчика:

{"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300}

Наш формат:

{"count": 5, "specie": "Тунец" , "avg_size": 30 }'''
