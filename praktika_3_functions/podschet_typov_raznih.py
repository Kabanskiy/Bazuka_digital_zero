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
            b = count(i)
            spisok += b
        return f'количество символов равно {spisok}'
    elif type(n) is int:
        for i in n:
            if i // 2 == 0:
                return f'количество нечетных цифр равно {chislo}'
            else:
                continue
    elif type(n) is str:
        for i in n:
            c = count(i)
            stroka += c
        return f'количество букв в строке равно {stroka}'
print(input())