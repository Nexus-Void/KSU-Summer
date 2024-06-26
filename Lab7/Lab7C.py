import pygame, sys
from pygame.locals import *

# Initializes Pygame
pygame.init()
# Manage any external resources, such as files or networking
# currently empty
# Manage any special functions or classes our game needs
rect1 = pygame.Rect(0, 0, 100, 100)
surf1 = pygame.Surface((rect1.width, rect1.height))
surf1.fill((0, 255, 0))

rect2 = pygame.Rect(0, 400, 100, 100)
surf2 = pygame.Surface((rect2.width, rect2.height))
surf2.fill((0, 0, 255))

direction = 1
# Initializes the Display's Surface and saves it
resolution = (1000, 500)
screen = pygame.display.set_mode(resolution)
# Creates the clock, so we can slow the game down
# to a manageable speed
clock = pygame.time.Clock()
# Main gameplay loop
while True:
    # Check which keys have been pressed
    keys = pygame.key.get_pressed()
    # Checks what events happened, and act on them.
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    # Paint the whole screen back
    screen.fill(color=(0, 0, 0))
    screen.blit(surf1, (rect1.x, rect1.y))
    screen.blit(surf2, (rect2.x, rect2.y))
    rect1 = rect1.move(5 * direction, 0)
    rect2 = rect2.move(5 * direction, 0)
    if rect1.x >= 900 or rect1.x <= -1:
        direction *= -1

    # Update the Display with the contents of the Display's surface
    pygame.display.flip()
    # Slow the game to update 60 times per second
    clock.tick(60)
