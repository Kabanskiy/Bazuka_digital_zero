class Rectangle:
    def area(self, a, b=None):
        if b is not None:
            print('Получился прямоугольник', a * b)
        else:
            print('Получился квадрат', a)


rectangle_a = Rectangle()
rectangle_a.area(10, 5)
