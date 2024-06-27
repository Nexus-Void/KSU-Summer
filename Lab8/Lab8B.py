import pygame, sys
from pygame.locals import *

pygame.init()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create rectangles 1 and 2
obstacle_rect = pygame.Rect(175, 0, 50, 400)
obstacle = pygame.Surface((obstacle_rect.width, obstacle_rect.height))

square_rect1 = pygame.Rect(175, 175, 50, 50)
square1 = pygame.Surface((square_rect1.width, square_rect1.height))
square1.fill(BLUE)

square_rect2 = pygame.Rect(175, 0, 50, 50)
square2 = pygame.Surface((square_rect2.width, square_rect2.height))
square2.fill(BLUE)

square_rect3 = pygame.Rect(175, 350, 50, 50)
square3 = pygame.Surface((square_rect3.width, square_rect3.height))
square3.fill(BLUE)

# direction of square
direction1 = 1
direction2 = 1
direction3 = 1

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    screen.fill(color=(0, 0, 0))
    screen.blit(obstacle, (obstacle_rect.x, obstacle_rect.y))
    screen.blit(square1, (square_rect1.x, square_rect1.y))
    screen.blit(square2, (square_rect2.x, square_rect2.y))
    screen.blit(square3, (square_rect3.x, square_rect3.y))

    # changes the direction when surf2 hits the border
    square_rect1 = square_rect1.move(5 * direction1, 0)
    if square_rect1.x >= 350 or square_rect1.x <= -1:
        direction1 *= -1

    square_rect2 = square_rect2.move(10 * direction2, 0)
    if square_rect2.x >= 350 or square_rect2.x <= -1:
        direction2 *= -1

    square_rect3 = square_rect3.move(20 * direction3, 0)
    if square_rect3.x >= 350 or square_rect3.x <= -1:
        direction3 *= -1

    squares = [square_rect1, square_rect2, square_rect3]

    x = obstacle_rect.collidelist(squares)
    if x > -1:
        obstacle.fill(GREEN)
    else:
        obstacle.fill(RED)

    pygame.display.flip()

    clock.tick(60)
