import pygame
from 

#initialize Pygame
pygame.init()

#asset library
screen = pygame.display.set_mode((1280, 720))

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
    #draw all elements
    #update everything
    pygame.display.update()
