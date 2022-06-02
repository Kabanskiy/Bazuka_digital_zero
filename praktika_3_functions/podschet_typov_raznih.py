# Если в функцию передаётся кортеж, то посчитать длину всех его слов
# Если список, то посчитать кол-во букв и чисел в нём
# Число – кол-во нечётных цифр
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
        return f'длина слов {kortezh}'
    elif type(n) is list:
        for i in n:
            if type(i) is str:
                stroka += len(i)
            elif type(i) is int:
                chislo += 1
        return f'букв {stroka}, чисел {chislo}'
    elif type(n) is int:
        for i in str(n):
            i = int(i)
            if i % 2 != 0:
                chislo += 1
        return f'нечетных цифр {chislo}'
    elif type(n) is str:
        return f'букв в строке {len(n)}'

print(raz(('Chuck Norris', 'Van Damme')))
print(raz([800, 'bazuka', 100500, 'boroda']))
print(raz(1534530))
print(raz('Schwarzenegger'))
