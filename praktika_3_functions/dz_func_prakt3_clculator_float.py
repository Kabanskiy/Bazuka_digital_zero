# Простейший калькулятор c введёнными двумя числами вещественного типа
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию)

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))
# c = input('Введи знак */-+: ')

def pluse(a, b):
    return a + b
def minuse(a, b):
    return a - b
def proizv(a, b):
    return a * b
def delen(a, b):
    if b == 0:
        print('Делить на 0 нельзя')
    else:
        return a / b

while True:
    x = input('Введи знак +-*/ или 0, чтобы завершить программу: ')
    if x == '0':
        break
    else:
        if x == '+':
            print(pluse(a, b))
        elif x == '-':
            print(minuse(a, b))
        elif x == '*':
            print(proizv(a, b))
        elif x == '/':
            print(delen(a, b))
