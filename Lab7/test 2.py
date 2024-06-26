import pygame, sys
from pygame.locals import *
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
surf1 = pygame.Surface((50,50))
surf1.fill((255,0,0))
rect1 = pygame.Rect(0,0,50,50)
direction = 1
clock = pygame.time.Clock()
# Main gameplay loop
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    if surf1 == width:

        direction *= -1
    screen.fill(color=(0,0,0))
    rect1 = rect1.move(5,0) # update the Rect’s position every time the loop iterates
    screen.blit(surf1, rect1.topleft) # paint the Surface onto the Display’s Surface at the new position
    pygame.display.flip()
    clock.tick(60)
