a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = int(input('введите третье число: '))

if a > b and a > c:
    print(a, 'самое большое число')
elif b > a and b > c:
    print(b, 'самое большое число')
else:
    print(c, 'самое большое число')