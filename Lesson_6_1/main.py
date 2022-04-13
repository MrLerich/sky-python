from pin import check_pin

print("Введите ваш пин-код")
user_input = input()
if check_pin(user_input):
    print("Такой пин-код подходит")
else:
    print("Такой пин-код НЕ подходит")