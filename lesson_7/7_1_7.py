employees = {}
text = """Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / главный инженер
Довлатова / Эмилия / Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог
Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог
Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик
Шанская / Аграфена / Семеновна / 116 404 / 7 июля 1982 года / +7 (954) 940-47-96 / психолог для рыб"""
text_list = text.split("\n")
for text in text_list:
    data = text.split(" / ")
    employees[data[0]] = {"f": data[0], "i": data[1], "o": data[2],
                          "pass": data[3], "birthday": data[4],
                          "phone": data[5], "position": data[6]}
# Не удаляйте код ниже, он важен для проверки!

for employee in employees.values():
  for key, value in employee.items():
      print(key, value)
  print("-")