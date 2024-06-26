import pygame, sys
from pygame.locals import *

pygame.init()

rect1 = pygame.Rect(175, 0, 50, 400)
surf1 = pygame.Surface((rect1.width, rect1.height))
surf1.fill((255, 0, 0))  # red

rect2 = pygame.Rect(175, 175, 50, 50)
surf2 = pygame.Surface((rect2.width, rect2.height))
surf2.fill((0, 0, 255))  # blue

direction = 1

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=(0, 0, 0))
    screen.blit(surf1, (rect1.x, rect1.y))
    screen.blit(surf2, (rect2.x, rect2.y))

    rect2 = rect2.move(5 * direction, 0)
    if rect2.x >= 350 or rect2.x <= -1:
        direction *= -1

    

    pygame.display.flip()

    clock.tick(60)
