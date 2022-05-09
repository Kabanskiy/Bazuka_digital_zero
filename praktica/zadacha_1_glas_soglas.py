# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
# В случае равенства вывести на экран все гласные буквы

st = input('Введите текст: ')

alph = 'ёуеыаоэяию'
gl = 0
sogl = 0
s_gl = ''

for i in st:
    if i in alph:
        gl += 1
        s_gl += i
    else:
        sogl += 1
if gl == sogl:
    print(s_gl)
print(gl)
print(sogl)