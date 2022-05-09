# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу

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

# c = 0
# with open(r'C:\Users\User\Desktop\spisok_classa.txt') as f:
#     sp = f.readlines()
#     for i in sp:
#         i.replace('\n', '')
#         i = i.split()
#         c = += int(name[2])
#         if int(name[2])<=3:
#             print(f'{name[0]} {name[1]} {name[3]})
#      print()
#      print(f'Средний балл: {c/len(sp)}')