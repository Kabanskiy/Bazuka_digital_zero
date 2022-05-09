# Создай список с любыми значениями и выведи первый, средний и последний элементы.

sp = ['terminator', 14, 'pastagoy', 50, 'zhidkiy pastagoy', -2, 'zhidkiy terminator', 800, 'stul', 0, 'zhidkiy stul']

dlina = len(sp)

if dlina % 2 == 0:
    print(sp[0], ',', 'Среднего нет', ',', sp[-1])
else:
    print(sp[0], ',', sp[dlina//2], ',', sp[-1])