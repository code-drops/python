import pygame

pygame.init()
white = 255, 255, 255
red = 255, 0, 0

height = 500
width = 1000
screen = pygame.display.set_mode((width, height))

x = 0
y = 0
changex = 1
changey = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.circle(screen, red, [x, y], 50)
    x += changex
    y += changey

    if y > height - 50:
        changey = -1
    elif y < 50:
        changey = 1
    if x > width - 50:
        changex = -1
    elif x < 50:
        changex = 1
    pygame.display.flip()
