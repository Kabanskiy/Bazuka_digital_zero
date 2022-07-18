import sqlite3

# Создаём Базу данных
conn = sqlite3.connect('name1.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
# если нужен не текст, а цифры, то пишем не TEXT. a INTENGER

# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''') # хэлоу в колонку 1, ворлд в колонку 2
# Сохраняем изменения
conn.commit()

d = "red"       # также может быть и инпут и рандом, главное, чтоб тип данной переменной
f = "black"     # соответствовал типу колонки, в которую будем вставлять
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES (?,?)''', (d, f)) # VALUES (?,?) - ставим вопросы, если не знаем что будем вставлять
conn.commit()

cursor.execute('''SELECT*FROM tab_1''') # * - говорит о том, что мы хотим достать все. Если бы стоял col1, то доставали бы col1
k = cursor.fetchall()
print(k)

# удаление записи из таблицы
# cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
# conn.commit()