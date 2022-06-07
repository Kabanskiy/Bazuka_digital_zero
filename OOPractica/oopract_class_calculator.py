# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций. А также функция, для ввода данных.

class Calc:

    def __init__(self):
        self.vvod()

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def proizv(self):
        return self.a * self.b

    def delen(self):
        if self.b == 0:
            return 'делить на ноль нельзя'
        else:
            return self.a / self.b

    def vvod(self):
        self.a = int(input('Введите первое число: '))
        self.b = int(input('введите второе число: '))

while True:
    ex = Calc()
    c = input('введите операцию (только +,-,*,/): ')

    if c == '+':
        print(ex.plus())
    elif c == '-':
        print(ex.minus())
    elif c == '/':
        print(ex.delen())
    elif c == '0':
        break
    else:
        print(ex.proizv())
