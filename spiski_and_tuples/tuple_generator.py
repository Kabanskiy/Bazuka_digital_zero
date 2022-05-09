import random

a = [random.randint(1, 100) for i in range(10)]
a = tuple(a)
print(a)
print(a.index(min(a)), a.index(max(a))) # можем применить index  к кортежу, т.к. она его не меняет, а лишь дает индексацию

# в выводе показывается основной принт и индексы запрашиваемых параметров