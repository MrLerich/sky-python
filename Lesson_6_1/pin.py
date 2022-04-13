# If it's not an integer it will raise a ValueError exception
def check_pin(pin):
    if pin.isdigit() and len(pin) == 4:
        return True
    else:
        return False

# # print(check_pin(1234))
#
# def check_pin(pin: str) -> bool:
#     try:
#         parsed_pin = int(pin)
#         pin_length = len(pin)
#         return pin_length == 4
#     except Exception:
#         return False

# код вашей функции должен быть выше

try:
    assert check_pin("1234") == True
    assert check_pin("123") == False
    assert check_pin("a000") == False
    assert check_pin("0000") == True
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")