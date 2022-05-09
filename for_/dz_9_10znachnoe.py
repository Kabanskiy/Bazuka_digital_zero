a = input('Введите 10значное число: ')
print('Четные числа: ')
b = 0
for i in a:
    b = int(i)
    if b % 2 == 0 and b != 0:
        print(b, end = ', ')
