import pygame, sys
from pygame.locals import *

# Initializes Pygame
pygame.init()
# Manage any external resources, such as files or networking
# currently empty
# Manage any special functions or classes our game needs
# currently empty
# Initializes the Display's Surface and saves it
resolution = (500, 500)
screen = pygame.display.set_mode(resolution)

surf1 = pygame.Surface((100, 100))
surf1.fill((255, 0, 0))  # red

surf2 = pygame.Surface((50, 50))
surf2.fill((0, 255, 0))  # green
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
    surf1.blit(surf2, (0, 0))
    screen.blit(surf1, (250, 250))
    # Update the Display with the contents of the Display's surface
    pygame.display.flip()
    # Slow the game to update 60 times per second
    clock.tick(60)
