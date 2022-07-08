# Два метода в классе, один принимает в себя либо строку, либо число
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа
# Длину строки и числа искать во втором методе

class Boroda:
    def __init__(self):
        self.glas = []
        self.sogl = []
        self.g = 0
        self.s = 0
        self.num = 0
    def first(self, a):
        if type(a) is str:
            for i in a:
                if i in 'eyuioaёуеыаоэяию':
                    self.g += 1
                    self.glas.append(i)
                else:
                    self.s += 1
                    self.sogl.append(i)
            print('Гласных: ', self.g)
            print('Согласных: ', self.s)
            print('Длина слова: ', self.second(a))
            if (self.g * self.s) <= self.second(a):
                print('Все согласные:', self.sogl)
            else:
                print('Все гласные:', self.glas)
        if type(a) is int:
            for i in str(a):
                i = int(i)
                if i % 2 == 0:
                    self.num += i
            print('Итого: ', self.num * self.second(a))

    def second(self, a):
        return len(str(a))

ex = Boroda()
vvod = input('Введите буквенные или цифровые значения: ')
if vvod.isalpha():
    ex.first(vvod)
elif vvod.isdigit():
    ex.first(int(vvod))
