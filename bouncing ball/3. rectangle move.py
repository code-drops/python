import pygame
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

x = 0
y = 0
change_x = 1
change_y = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.rect(screen, red, [x, y, 50, 50])
    x = x + change_x
    y = y + change_y
    if y > 450 or y < 0:
        change_y = change_y * -1
    if x > 950 or x < 0:
        change_x = change_x * -1
    pygame.display.flip()