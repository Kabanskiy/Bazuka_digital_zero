# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность

with open('input.txt', 'w') as f:
    f.write(input())

with open('input.txt', 'r') as f:
    for line in f:
        c = line.split()
        a = int(c[0])
        b = int(c[1])
        break

k = a - b

with open('output.txt', 'w') as f:
    k = str(k)
    f.write(k)