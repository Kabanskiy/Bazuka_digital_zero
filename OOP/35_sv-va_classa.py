class Car:
    # Статические поля (переменные класса)
    default_color = 'Grey'
    default_weight = 5000

    def __init__(self, color, model):
        # Динамические поля (переменные объекта)
        self.color = color
        self.model = model

    def turn_on(self):
        pass

    def ride(self):
        pass


car_object = Car('red', 'BMW')

print(car_object.default_color)
print(car_object.color)

print(dir(Car))


class Class1(object):

    def __init__(self, value):
        self.__var = value

    def getVar(self):  # Чтение
        return self.__var

    def setVar(self, value):  # Запись
        self.__var = value

    def delVar(self):  # Удаление
        del self.__var

    v = property(getVar, setVar, delVar, "Строка документирования")

c1 = Class1(5)

c1.v = 35  # Вызывается метод setVar()
print(c1.v)  # Вызывается метод getVar()
del c1.v  # Вызывается метод delVar()
