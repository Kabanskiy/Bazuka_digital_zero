a = {1: [1, 2, 3], 2: 'hey'}

for key, value in a.items():
    print(f'Ключ: {key}, значение: {value[1]}')
# print(a.items()) # выводится список кортежей с парами ключ:значение. Перед скобками будет стоять dict_items
# print(a.values())
# print(a.keys())
# print(a.clear())
# b = a. copy()
# print(id(a), id(b))
# print(b)
# a.pop(2) # указываем ключ, котоый хотим удалить
# print(a)
# del a[1]
# print(a)
# if 1 in a:
#     print('на месте')
# a = [1, 2, 3]
# b = ['х', 'у', "й"] # становятся ключами в сл
# c = dict(zip(a, b)) # становятся значениями в сл
# print(c)
# # Можно так же напрямую в одну строку:
# c = dict(zip([1, 2, 3], ['х', 'у', "й"]))
# print(c)