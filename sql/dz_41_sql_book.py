# Домашнее задание
# 1.Сформулируйте SQL запрос для создания таблицы book. Структура таблицы book:
# 2.Занесите новую строку в таблицу book
# 3.Выбрать информацию о всех книгах из таблицы book.

import sqlite3

conn = sqlite3.connect('book.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT)''')
cursor.execute('''INSERT INTO book(col_1,col_2) VALUES ('book_id','INT PRIMARY KEY AUTO_INCREMENT'),
('title','VARCHAR(50)'), ('author','VARCHAR(30)'), ('price','DECIMAL(8, 2)'), ('amount','INT')''')
cursor.execute("INSERT INTO book(col_1,col_2) VALUES ('Chuck','Norris')") # вносим новую строку
conn.commit()

cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
# print(k)
for i in k:
    i = list(i) # преобразовали в список
    h = 0
    print(' '.join(str(h) for h in i))