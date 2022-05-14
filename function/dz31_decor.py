# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

def deco(fn):
    global skoko_raz
    skoko_raz += 1
    print('nachalo')
    fn()
    print('konets')
    print(skoko_raz)
skoko_raz = 0

@deco
def test1():
    print('testim1')

@deco
def test2():
    print('testim2')

@deco
def test3():
    print('testim3')