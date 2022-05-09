# person = {'name': 'Ya', 'age': 30, 'city': 'Minsk'}
# print(person['age'])

magaz = {
    'navaga': [3.30, 35],
    'pork': [14.00, 6],
    'beef': [17.10, 7],
    'sugar': [150.50, 1],
    'tampax':[99.99, 2]
}

for key, value in magaz.items():
    print(key, '-', value[0], '-', value[1])

summa = 0 # описание ниже
while True:
    korzina = input('Интересующий товар или n для выхода: ')
    if korzina == 'n' or korzina not in magaz: # в данном случае корзина выступает именем ключа, который ищем в магазе
        break
    kolichestvo = int(input('Интересующее количество: '))
    if kolichestvo > magaz[korzina][1]: # обращаемся к словарю magaz по ключу korzina и в значение 1, т.к. у нас список
        print('Столько нет, выбери другое количество или другой товар')
        continue # пропускаем, чтобы искать заново
    summa = summa + (kolichestvo * magaz[korzina][0]) # сумма товара так же как в line 20, и чтобы при итерации цикла посчиталась сумма всех покупок, складываем в переменной сумм
    # теперь нужно убрать уже купленные товары из магаза
    magaz[korzina][1] -= kolichestvo # при покупке нового товара будем отнимать то количество, которое купили
print(f'к оплате: {summa} руб.')

for key, value in magaz.items():              # выводим, чтобы видеть сколько чего осталось в магазе
    print(key, '-', value[0], '-', value[1])


