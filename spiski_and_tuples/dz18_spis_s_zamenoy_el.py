# Создай список, замени первый его элемент на [1, 2, 3], затем в конец списка добавь сумму элементов вложенного списка.

spis = ['dorou', 'terminator', 100500, 'pzkfw panther', 777]

x = [1, 2, 3]
spis[0] = x

# x = str(spis)
summa = 0
for i in x:
    summa += int(i)
spis.extend([summa])
print(spis)







# summa = [x[0] + x[1] + x[2]]
#
# # summa = [sum(x)]            Проще всего так, правда мы это еще не проходили