# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

def deco(fn):
    global skoko_raz
    skoko_raz += 1
    print('Наверное')
    fn()
    print('Круче')
    print(skoko_raz)
skoko_raz = 0

@deco
def test1():
    print('Джеки Чан')
@deco
def test2():
    print('Чак Норрис')