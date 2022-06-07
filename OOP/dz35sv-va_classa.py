# Допишите по 2 динамических и статических свойства в класс с предыдущего задания. Продемонстрируйте их работу

class Terminator:
    kiber_skelet = 'metall'
    kiber_zadacha = 'John Connor'
    def __init__(self, skelet, model):
        self.skelet = skelet
        self.model = model

    def dict(self):
        pass
    def str(self):
        pass

term_kiborg = Terminator('Arni', 'Ciberdain Systems')

print(term_kiborg.kiber_skelet)
print(term_kiborg.skelet)

# print(dir(Terminator))
# t800 = Terminator
# print(t800)
#
# t800_101 = Terminator()
# t800_101.print()