'''Создайте файл main.py с содержанием:

f = open('mydata.txt', 'r')
content = f.read()
f.close

C помощь терминала убедитесь, что рядом нет никакого файла mydata.py.

Запустите программу из командной строки.'''


f = open('mydata.txt', 'r')
f.write("Теперь тут новые данные!")
f.close