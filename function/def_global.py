def fun1():
    global a # еременная будет использоваться в любой части ф-и и будет равна тому значению, кот указ после глобал
    a = 5
    return a + 6
def fun2():
    return a + 10

print(fun1())
print(fun2())