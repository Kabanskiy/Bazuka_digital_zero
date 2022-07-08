class Example:
    def print(self): # селф это ссылка
        print('dorou')

ex = Example() # создaли объект ех класса эксампл
print(ex) # так мы получим область памяти, в которой хранится эксампл обжект(наш класс)
ex_1 = Example()
ex_1.print()

# создали класс. А объектов можно сделать множество


 # Пример простейшего класса, который ничего не делает
class A:
    pass

a = A()
b = A()

a.arg = 1 # у экземпляра a появился атрибут arg, равный 1
b.arg = 2 # а у экземпляра b - атрибут arg, равный 2

print(a.arg)
#Результат: 1

print(b.arg)
#Результат: 2

c = A()
print(c.arg) # а у этого экземпляра нет arg

#Результат: Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#AttributeError: 'A' object has no attribute 'arg'


#Теперь мы можем создать несколько экземпляров этого класса:

a = A()
b = A()

a.arg = 1 # у экземпляра a появился атрибут arg, равный 1
b.arg = 2 # а у экземпляра b - атрибут arg, равный 2

print(a.arg)
#Результат: 1

print(b.arg)
#Результат: 2

c = A()
print(c.arg) # а у этого экземпляра нет arg
#Результат: Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#AttributeError: 'A' object has no attribute 'arg

# Классу возможно задать собственные методы:

class A:
    def g(self): # self - обязательный аргумент, содержащий в себе экземпляр класса,
# передающийся при вызове метода, поэтому этот аргумент должен присутствовать во всех методах класса.

        return 'hello world'

a = A()
a.g()
#Результат: 'hello world'

# Еще пример:
class B:
    arg = 'Python' # Все экземпляры этого класса будут иметь атрибут arg, равный "Python"
# Но впоследствии мы его можем изменить
    def g(self):
        return self.arg

b = B()
b.g()
#Результат: 'Python'

B.g(b)
#Результат: 'Python'

b.arg = 'spam'
b.g()
#Результат: 'spam
