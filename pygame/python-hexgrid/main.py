import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption('Hexgrid')

pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEY_PRESS:
            if event.key ==
