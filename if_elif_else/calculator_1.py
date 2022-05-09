# Primitive Calculator. User types numbers with keyboard and recepts of result
a = float(input('Введите первое число: '))          # Вводим как знаки
c = input('введите операцию (только +,-,*,/): ')    # Водим как строку
b = float(input('введите второе число: '))          # Вводим как знаки
                                                    # Далее, с помощью if сравниваем строки и знаки
if c == '+':                                        # В кавычках, потому что тип данных строки str
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '/':
    print(a/b)
else:
    print(a*b)