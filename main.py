import pygame
from sys import exit

#initialize Pygame
pygame.init()

#asset library
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Function to Date')
clock = pygame.time.Clock()

test_surface = pygame.Surface((720, 500))
test_surface.fill("Red")
main_bg = pygame.image.load("graphic/assets/mainbg.png")

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    screen.blit(main_bg,(0, 0))
    screen.blit(test_surface,(60, 60))

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60
