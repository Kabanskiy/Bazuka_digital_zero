# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше, то обновить 1 запись в первой таблице на «hello»

import sqlite3

conn = sqlite3.connect('Dve_tablitsi.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
conn.commit()
sp = ['Chuck Norris', 100, 500, 'Terminator', 1, 'Zhak If Kusto']
for i in sp:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (i,))
        conn.commit()
        dlina_slova = len(i)
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (dlina_slova,))
        conn.commit()
    elif type(i) is int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES ('нечетное')''')
            conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
summ = 0
for j in k:
    summ+=1
    if summ > 5:
        cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
        conn.commit()
    else:
        cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')
        conn.commit()

# проверка

cursor.execute('''SELECT * FROM tab_1''')
x = cursor.fetchall()
cursor.execute('''SELECT * FROM tab_2''')
y = cursor.fetchall()
print(x)
print(y)