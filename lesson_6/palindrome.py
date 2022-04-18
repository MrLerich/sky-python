'''
Создайте файл palindrome.py в нем функцию is_palindrome(word)

Функция должна возвращать True, если слово палиндром, иначе False.

Чтобы проверить является ли срока палиндромом, уберите из нее пробелы, приведите к нижнему регистру, затем проверьте, что инвертированная строка (reversed_str = str[::-1]) равна оригинальной строке, например:

level – True

sagas – True

hero – False

drama – False

Для проверки скопируйте этот код под функцию и запустите файл.

# код вашей функции должен быть выше

try:
  assert is_palindrome("level") == True
  assert is_palindrome("sagas") == True
  assert is_palindrome("hero") == False
  assert is_palindrome("drama") == False

except AssertionError:
  print("Неверно, проверьте функцию на разных значениях")

else:
  print("Все хорошо, все работает")'''

def is_palindrome(word):
    # word = input().strip().lower()
    reversed_word = word[::-1]
    if word == reversed_word:
      return True
    else:
      return False

try:
  assert is_palindrome("level") == True
  assert is_palindrome("sagas") == True
  assert is_palindrome("hero") == False
  assert is_palindrome("drama") == False

except AssertionError:
  print("Неверно, проверьте функцию на разных значениях")

else:
  print("Все хорошо, все работает")