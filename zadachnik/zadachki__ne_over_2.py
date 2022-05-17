rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.
for position in range(11):
    print('^' * 27)
    for letter in rus_lower:
        if rus_lower.index(letter) % 11 == position:
            print('| ', letter.upper(), letter, ' |', end='')
    print()
print('^' * 27)
