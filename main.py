import pygame
from sys import exit

#initialize Pygame
pygame.init()

#color library
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (127, 0 , 255)
orange = (255, 165, 0)

#asset library
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Function to Date')
clock = pygame.time.Clock()

background = pygame.image.load('Assets/FtD_BG.png')

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #draw all elements
    #update everything
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60
