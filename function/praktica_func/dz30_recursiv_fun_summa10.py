# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100

import random

def sum(x):
    if x == 0:
        return 0
    else:
        print(x)
        return x + sum(x-1)
print(sum(random.randint(1,100)))


#[random.randint(1,100)]