# Допишите несколько атрибутов в класс с прошлого задания, продемонстрируйте их работу

class Terminator:
    def print(self):
        print('bazuka')
    def dict(self):
        print('Arni')
    def str(self):
        print('жидкий терминатор')

print(dir(Terminator))
t800 = Terminator
# print(t800)
#
# t800_101 = Terminator()
# t800_101.print()