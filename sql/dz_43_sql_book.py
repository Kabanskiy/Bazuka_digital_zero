# Домашнее задание
# 1.Сформулируйте SQL запрос для создания таблицы book. Структура таблицы book:
# 2.Занесите новую строку в таблицу book
# 3.Выбрать информацию о всех книгах из таблицы book.

import sqlite3

conn = sqlite3.connect('book.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT, INTEGER) ''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('book_id','INT PRIMARY KEY AUTO_INCREMENT'),
INSERT INTO tab_2(col_1,col_2) VALUES ('title','VARCHAR(50)'),
INSERT INTO tab_3(col_1,col_2) VALUES ('author','VARCHAR(30)'),
INSERT INTO tab_4(col_1,col_2) VALUES ('price','DECIMAL(8, 2)'),
INSERT INTO tab_5(col_1,col_2) VALUES ('amount','INT'),
INSERT INTO tab_6(col_1,col_2) VALUES ('Chuck','Norris')''')
conn.commit()

