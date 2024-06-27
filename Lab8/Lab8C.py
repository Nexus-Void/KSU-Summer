import pygame, sys
from pygame.locals import *

pygame.init()

player = pygame.Rect((235, 235, 50, 50))
surf1 = pygame.Surface((player.width, player.height))
surf1.fill((0, 0, 255))
resolution = (500, 500)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player.move(0, -5)

    screen.fill(color=(0, 0, 0))
    screen.blit(surf1, (player.x, player.y))

    pygame.display.flip()

    clock.tick(60)
