# Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные задайте статически, две динамически
# ❖ Первая функция: создайте переменную и выведите её
# ❖ Вторая функция: верните сумму 2-ух глобальных переменных
# ❖ Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную.
# ❖ Создайте объект класса.
# ❖ Напечатайте обе функции.
# ❖ Напечатайте переменную a.
class Example:
    a = 2
    b = 3

    def __init__(self, r, d):
        self.r = r
        self.d = d

    def first(self):
        self.first = 10
        print(self.first)

    def second(self):
        return self.a + self.b

    def thirth(self):
        return self.r**self.d

ex = Example(4, 6)
ex.first()
print(ex.second())
print(ex.thirth())
print(ex.a)
