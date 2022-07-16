# Создайте новую Базу данных
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое число
# Число запрашивается с клавиатуры, а слова задаются статически.
# Выведите каждую запись в отдельную строку

import sqlite3

conn = sqlite3.connect('this_file.db')

cursor = conn.cursor()
chislo = int(input())
# Создадим таблицу с тремя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT, col_3 INTEGER) ''')
# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2, col_3) VALUES ('Chuck','Norris', ?)''', (chislo,))
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

# теперь выводим все в отдельную строку
for i in k:
    i = list(i) # преобразовали в список
    h = 0
    print(' '.join(str(h) for h in i)) # с помощью join и встроенного for перебрали список на отдельные значения
# так как Chuck, Norris, и 5 - разные типы данных, их нужно перебирать с помощью str
# поэтому вывели каждую строку, сначала сняв список, затем кортеж