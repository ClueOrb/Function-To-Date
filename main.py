import pygame
from sys import exit

#initialize Pygame
pygame.init()

#main setup (Screen, Title, FPS)
screen = pygame.display.set_mode((1280, 720), 0)
pygame.display.set_caption('Function to Date')
framerate = 60
clock = pygame.time.Clock()

#screen assets
test_surface = pygame.Surface((720, 500))
test_surface.fill("Black")
background = pygame.image.load("graphic/assets/mainbg.png")

#variables
font = pygame.font.Font("freesansbold.ttf", 16)

#functions
def draw_monitor():
   pygame.draw.rect(test_surface, "Blue", [250, 250, 200, 170])

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    screen.blit(background,(0, 0))
    screen.blit(test_surface,(60, 60))
    draw_monitor()
    pygame.display.update()
    clock.tick(framerate)  # limits FPS to 60
