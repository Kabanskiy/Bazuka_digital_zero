# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os

import os

# os.mkdir(r'C:\Users\User\Desktop\Chuck Norris')
os.chdir(r'C:\Users\User\Desktop\Chuck Norris')

# a, b, c = open('test_1.txt', 'w'), open('test_2.txt', 'w'), open('test_3.txt', 'w')
# a.close(), b.close(), c.close()
# os.rename('test_1.txt', 'rename_1.txt'), os.rename('test_2.txt', 'rename_2.txt'), os.rename('test_3.txt', 'rename_3.txt')
# a.close(), b.close(), c.close()
# os.remove('rename_1.txt'), os.remove('rename_2.txt'), os.remove('rename_3.txt')

os.chdir(r'..')
print(os.getcwd())
os.rmdir('Chuck Norris')


