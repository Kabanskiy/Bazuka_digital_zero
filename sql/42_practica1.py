# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД

import sqlite3
import random

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER)''')
a = random.randint(0,9)
b = random.randint(0,9)

#Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES(?,?)''',(a,b))
conn.commit()

cursor.execute('''SELECT col_1, col_2 FROM Tab_1''') # выводим без учета id
k = cursor.fetchall()
print(k)

sum = 0 # собираем сумму
for i in k:
    for j in i:
        sum+=j
sred_arif = sum/(len(k)*2) # среднее арифметическое. len - количество пар выводимых кортежей. * на 2, т.к. по два числа на пару
print(sum)
print(sred_arif)

if sred_arif > len(k):
    cursor.execute('''DELETE FROM Tab_1 WHERE id = 4''')
    conn.commit()

cursor.execute('''SELECT col_1, col_2 FROM Tab_1''') # выводим без учета id
k = cursor.fetchall()
print(k)