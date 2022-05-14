# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

def deco(fn):
    global skoko_raz
    skoko_raz += 1
    print('Navernoe')
    fn()
    print('kruche')
    print(skoko_raz)
skoko_raz = 0

@deco
def test1():
    print('Chuck Norris')

@deco
def test2():
    print('Jackie Chan')