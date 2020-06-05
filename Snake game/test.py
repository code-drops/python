import pygame
import random

# initialize the pygame
pygame.init()

# setting the width and height of the screen
display_width = 600
display_height = 400
surface = pygame.display.set_mode((display_width,display_height))

# setting colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#game variables
clock = pygame.time.Clock()


# setting the caption of the screen
pygame.display.set_caption("Snake Game")


# display text on screen

def displayText(text,color,x,y,fontSize):
    font = pygame.font.SysFont(None,fontSize)
    screen_text = font.render(text,True,color)
    surface.blit(screen_text,[x,y])

# plotting snake
def plotSnake(surface,color,snakeList,size):
    for x,y in snakeList:
        pygame.draw.rect(surface, black, (x, y, size, size))


def gameLoop():

    # game variables
    x = 100
    y = 100
    size = 15
    fps = 25
    score = 0
    snakeSensitive = 10
    changeX = 0
    changeY = 0
    snakeList = []
    snakeLength = 1

    # random food
    foodX = random.randint(50, display_width - 50)
    foodY = random.randint(50, display_height - 50)
    gameOver = False
    while gameOver == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changeX = 10
                    changeY = 0
                if event.key == pygame.K_LEFT:
                    changeX = -10
                    changeY = 0
                if event.key == pygame.K_UP:
                    changeY = -10
                    changeX = 0
                if event.key == pygame.K_DOWN:
                    changeY = 10
                    changeX = 0
        x = x + changeX
        y = y + changeY

        if x<0 or x>display_width or y<0 or y>display_height:
            gameOver = True

        if abs(x - foodX) < snakeSensitive and abs(y - foodY) < snakeSensitive:
            score = score + 1
            pygame.display.set_caption("Score : " + str(score * 10))
            foodX = random.randint(50, display_width - 50)
            foodY = random.randint(50, display_height - 50)
            snakeLength += 1

        head = []
        head.append(x)
        head.append(y)
        # 2d list to store the x,y cordinates that are appended whenever snake eats food
        snakeList.append(head)

        if len(snakeList) > snakeLength:
            snakeList.pop(0)


        surface.fill(white)
        pygame.draw.rect(surface, red, (foodX, foodY, size, size))
        plotSnake(surface, black, snakeList, size)
        pygame.display.update()
        clock.tick(fps)

gameLoop()

while True:
    surface.fill(white)
    score = pygame.display.get_caption()
    displayText("Game Over", red, 200, 50,50)
    if score[0] == "Snake Game":
        displayText("Score : " + str(0), red, 240, 125, 30)
    else:
        displayText("Score :" + score[0][7:], red, 20, 125, 30)
    displayText("Press p to play again",red,150,300,50)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_p:
                gameLoop()
