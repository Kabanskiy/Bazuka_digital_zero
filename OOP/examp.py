class Example: # класс, имя класса, двоеточие
    # pass # пропускаем чать кода
    def print(self): # создали метод деф. Отныне здесь будет фигурировать селф - это ссылка
        print('zdarova')
# теперь создается объект, который будет выполнять ф-ю класса

ex = Example # объект ех класса эксампл
# чтобы вывать метод к объекту, мы пишем имя объекта . и вызывем  метод
# print(ex) # запустится область памяти, в которой хранится эксампл обджект. Получаем область, в которой ех, явлся объектом класса эксампл
ex_1 = Example()
ex_1.print()
# теперь есть два объекта ех и ех_1, которые в себя вызывают метод принт

# объектов мб неогр кол-во
