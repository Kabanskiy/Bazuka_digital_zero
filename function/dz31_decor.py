# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

def deco(fn):
    print('nachalo')
    fn()
    print('konets')

@deco
def test1():
    print('testim1')

@deco
def test2():
    print('testim2')