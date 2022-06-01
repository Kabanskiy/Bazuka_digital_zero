# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.

def raz(n):
    if type(n) == tuple():
        return len(n)
    elif type(n) == list():
        return count(n)
    elif type(n) == int():
        return int(n)
    elif type(n) == str():
        return count(n)