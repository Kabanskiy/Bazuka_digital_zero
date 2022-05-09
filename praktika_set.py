a = {2, 3, 95, 4, 7, 10}
b = frozenset([6, 9, 12, 95, 4, 10])

# объединение
print(a.union(b)) # все хранится в а
c = a|b
print(c)

# пересечение
print(a&b)
print(a.intersection(b)) # все хранится в а

# итерация
for i in b:
    print(i)


