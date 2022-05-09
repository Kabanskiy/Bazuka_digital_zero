# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран

di = {'a' : 3, 'b' : 1, 'c' : 8, 'd' : 2, 'e' : 10}

proizv = 1

for key, value in di.items():
    proizv = proizv * value
print(proizv)
