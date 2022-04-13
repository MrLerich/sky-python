# store = {
#     "apples": {"name":"Яблоки", "price":"100", "available": 40},
#     "oranges": {"name":"Апельсины", "price":"200", "available": 20},
#     "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
# }
#
# for item in store.items():
#   print(item["name"], item["price"])


store = {
    "apples": {"name":"Яблоки", "price":"100", "available": 40},
    "oranges": {"name":"Апельсины", "price":"200", "available": 20},
    "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
}

for key in store:
  print(item[key]["name"], item[key]["price"])