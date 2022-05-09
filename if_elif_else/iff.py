number = 23
guess = int(input('введи число: '))

if guess == number:
    print('маладэц ежи, ')
    print('тока пирога не буит')
elif guess < number:
    print('нэт, число больше')
else:
    print('нэт, число меньше')