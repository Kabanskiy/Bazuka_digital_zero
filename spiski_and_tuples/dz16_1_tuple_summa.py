import random

a = [random.randint(0, 10) for i in range(10)]
a = tuple(a)
print(a)
print(sum(a))

