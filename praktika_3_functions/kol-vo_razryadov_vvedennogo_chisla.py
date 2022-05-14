# Написать функцию, которая определяет количество разрядов введенного целого числа.

def skynet(num):
    i = 0
    while num > 0:
        num = num // 10
        i += 1
    return i
print(skynet())
