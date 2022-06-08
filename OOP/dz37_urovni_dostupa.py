# Продемонстрируйте разные уровни доступа на примере любого класса

class Diareya:
    chair = 'Это нормальный стул'
    _chair = 'Это жидкий стул'
    __chair = 'А это совсем жидкий стул, мы не будем его показывать'

ex = Diareya()
print(ex.chair)
print(ex._chair)
print(ex._Diareya__chair)