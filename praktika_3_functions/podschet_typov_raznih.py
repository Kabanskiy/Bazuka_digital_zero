# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.

def raz(n):
    kortezh = 0
    spisok = 0
    chislo = 0
    stroka = 0
    if type(n) is tuple:
        for i in n:
            a = len(i)
            kortezh += a
        return f'длина слов равна {kortezh}'
    elif type(n) is list:
        for i in n:
            a =
        return count(n)
    elif type(n) == int():
        return int(n)
    elif type(n) == str():
        return count(n)
print()