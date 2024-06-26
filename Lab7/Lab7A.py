import pygame, sys
from pygame.locals import *
# Initializes Pygame
pygame.init()
# Manage any external resources, such as files or networking
# currently empty
# Manage any special functions or classes our game needs
# currently empty
# Initializes the Display's Surface and saves it
resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
color = 0
surf1 = pygame.Surface((400, 400))
surf1.fill((color, color, color))
direction = 1
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
    surf1.fill((color, color, color))
    screen.blit(surf1, (0, 0))
    if color > 254 or color <= 0:
        direction *= -1
    if direction == -1:
        color -= 1
    else:
        color += 1
    if color < 0:
        color = 0
    # Update the Display with the contents of the Display's surface
    pygame.display.flip()
    # Slow the game to update 60 times per second
    clock.tick(60)
