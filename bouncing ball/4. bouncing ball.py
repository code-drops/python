import pygame
pygame.init()

width = 1000
height = 500

# setting the window size
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
x = 50
y = 50
movex = 1
movey = 1
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:             # for clicking cross
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.circle(screen,black,(x,y),50)
    x = x + movex
    y = y + movey

    # for keeping ball within height
    if y > height-50 or y < 50:
        movey = movey * -1

    # for keeping ball within width
    if x > width-50 or x < 50:
        movex = movex * -1

    # updating the screen
    pygame.display.update()
