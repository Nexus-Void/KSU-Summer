import pygame, sys
from pygame.locals import *
# Initializes Pygame
pygame.init()
# Manage any external resources, such as files or networking
# currently empty
# Manage any special functions or classes our game needs
# currently empty
# Initializes the Display's Surface and saves it
resolution = (600, 600)
screen = pygame.display.set_mode(resolution)

box1 = pygame.Surface((60, 60))
box1.fill((255, 0, 0))
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
    screen.blit(box1, (0, 0))
    screen.blit(box1, (540, 0))
    screen.blit(box1, (0, 540))
    screen.blit(box1, (540, 540))
    screen.blit(box1, (270, 270))
    # Update the Display with the contents of the Display's surface
    pygame.display.flip()
    # Slow the game to update 60 times per second
    clock.tick(60)
