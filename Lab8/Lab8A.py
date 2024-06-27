import pygame, sys
from pygame.locals import *

pygame.init()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create rectangles 1 and 2
rect1 = pygame.Rect(175, 0, 50, 400)
obstacle = pygame.Surface((rect1.width, rect1.height))

rect2 = pygame.Rect(175, 175, 50, 50)
square = pygame.Surface((rect2.width, rect2.height))
square.fill(BLUE)  # blue

# direction of surf2
direction = 1

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    screen.fill(color=(0, 0, 0))
    screen.blit(obstacle, (rect1.x, rect1.y))
    screen.blit(square, (rect2.x, rect2.y))

    # changes the direction when surf2 hits the border
    rect2 = rect2.move(5 * direction, 0)
    if rect2.x >= 350 or rect2.x <= -1:
        direction *= -1

    if rect2.colliderect(rect1):
        obstacle.fill(GREEN)
    else:
        obstacle.fill(RED)

    pygame.display.flip()

    clock.tick(60)
