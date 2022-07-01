class Example:
    def print(self):
        print('dorou')

print(dir(Example)) # с помощью дир получаем список всех атрибутов нашего класса
# '__встроенные атрибуты__'
ex = Example()
ex_1 = Example()
# ex_1.print()

# Метод '__init__' является инициализатором
# '__new__' - конструктор создается в этом методе
# в самом конце появился 'print' - польз атрибут появл с таким же именем, которое дали мы

# пример:
# class Rectangle:
# default_color = "green"
#
# def __init__(self, width, height):
# self.width = width
# self.height = height
# default_color – это
# статический атрибут, и доступ к нему, как было сказано выше, можно получить не создавая объект класса Rectangle
# width и height – это динамические атрибуты, при их создании было использовано ключевое слово self.

