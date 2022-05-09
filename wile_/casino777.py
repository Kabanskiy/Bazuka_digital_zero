# Казино. Числа от 1 до 10 и цвета от 1 до 2( 1 - красный, 2 - чёрный). У пользователя 5 попыток

import random

a = random.randint(1, 10)
b = random.randint(1, 2)

i = 0

while i < 5:
    i = i + 1 # i += 1
    c = int(input('input numbers 1 - 10: '))
    d = int(input('input color 1 - red, 2 - black: '))
    if a == c and b == d:
        print(f'You win!: {c}{d}')
        break
    elif a != c and b == d:
        print(f'You do not guess number: {c}, but you guess color: {d}')
    elif a ==c and b != d:
        print(f'You do not guess color: {d}, but you guess number: {c}')
    else:
        print(f'You do not guess nothing. Try again')
else:
    print('Game over')