import os

# os.rename('3.py', '2.py') # переименование файла
# os.mkdir('txt') # создание новой папки
# os.chdir('txt') # изменение директории. Перемещение в указанный кталог
# os.chdir('..') # каталог назад. Если ввести еще раз, еще раз назад
# os.makedirs('raz/dva/tri') # создание нескольких папок в текущем местоположении
# os.remove('1.py') # удаление файла в текущей папке
# os.removedirs('raz/dva/tri') # удаление указанных папок
# os.rmdir('txt') # удаление указанной папки
# print(os.getcwd()) # просмотр текущего местонахождения в консоли

# Ниже Теория функции файлов

# os.mkdir('folder')
# if not os.path.isdir('folder'):
#     os.mkdir('folder')
# Функция os.path.isdir() вернет True, если переданное имя ссылается на существующий каталог

os.chdir('folder')
print('Текущая директория: ', os.getcwd())

# создание файла
tekst_moy = open('textos.txt', 'w')
# запись текста в этот файл
tekst_moy.write('this is text file')