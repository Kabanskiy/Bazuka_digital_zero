# С клавиатуры вводится 7-значное число. Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 цифры.

st = input('Введите 7-значное число: ')

ch = 0
nech = 0
spis = int()

for i in st:
    i = int(i)
    if i % 2 == 0:
        ch += 1
        spis += i
    else:
        nech += 1
        spis += i
if ch > nech:
    print(spis)
else:
    print(int(st[0])*int(st[2])*int(st[5]))
