import random

str_ = 'zdarova, goblin'

a = random.random()
b = random.uniform(5, 50)
c = random.randint(100, 1000)
d = random.choice(str_)

print('от 0 до 1: ', a, 'float: ', b, 'int: ', c, 'символ: ', d)
# print(a) показывает псевдорандомное вещественное число от 0 до 1
# print(b) показывает псевдорандомное вещественное число "от" и "до"
# print(c) показывает псевдорандомное целое число "от" и "до"
# print(d) показывает псевдорандомные символ, строку, список или кортеж
