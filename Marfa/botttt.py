f = open(r'C:\Users\User\Desktop\spisok_classa.txt')
suma = 0
n = 0
s = f.readlines()
for i in f:
    i = i.replace('\n', '')
    g = int(i[len(i)-2])
    suma += g
    n += 1
    if g < 3:
        print(i[:-1])
print('Средний балл: %.2f' % (suma / n))
