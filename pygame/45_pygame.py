import pygame

# инициализируем пайгейм
pygame.init()
# создаем цвета и их характеристики
white = (255, 255, 255)  # пробеливаем экран
blue = (0, 0, 255)
red = (255, 0, 0)
# создаем экран и указываем размеры
dis = pygame.display.set_mode((800, 500))
# создаем название игры
pygame.display.set_caption("Snake")

# заводим указатель на окончание игры
game_over = False

# задаем двиджение
x1 = 350
y1 = 450

x1_change = 0
y1_change = 0

# время
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # если кнопка влево, то х двигается
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:  # если кнопка вправо, то х двигается
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:  # если кнопка вверх, то y двигается
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:  # если кнопка вниз, то у двигается
                x1_change = 0
                y1_change = 10

    # здесь код завершения игры в случае касания конца экрана
    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    # здесь мы изменяем первоначальное значение 350 и 450 на значение в цикле, куда будет двигаться змейка
    x1 += x1_change
    y1 += y1_change
    dis.fill(white) # закрашивает экран из черного в белый

    pygame.draw.rect(dis, blue, (200, 150, 10, 10))
    pygame.display.update()

    clock.tick(30)

pygame = quit()
quit()
