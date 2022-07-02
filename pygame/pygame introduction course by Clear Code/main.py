import pygame
from sys import exit
screen = pygame.display.set_mode([800, 400]) # initialise display surface
pygame.display.set_caption('Game') # set name for pygame window
clock = pygame.time.Clock() # create clock object from pygame

test_surface = pygame.Surface([100, 200])
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all out elements
    screen.blit(test_surface, [200, 100])
    # update everything
    pygame.display.update()
    clock.tick(60)