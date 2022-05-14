def decore1(fn):
    print('Startuem')
    fn()                # здесь появляется функция, которую пишем далее
    print('Stopuem')

@decore1 # говорит о том, что мы используем указанный декоратор
def odin():
    print('Test1')

@decore1
def dva():
    print('test2')
# причем отдельно вызов этих функций не требуется

#Либо, если просто:
#
# def odin():
#     print('Test1')
#
# def dva():
#     print('test2')
#
# def decore1(fn):
#     print('Startuem')
#     fn()                # здесь появляется функция, которую вызываем далее
#     print('Stopuem')
# decore1(odin)           # и здесь уже как обычно вызываем функцию
# decore1(dva)
