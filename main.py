import pygame, time
from sys import exit

#----Initialize Pygame----#
pygame.init()

#---Main set up (Screen, Title, FPS)---#
screen = pygame.display.set_mode((1280, 720), 0)
pygame.display.set_caption('Function to Date')
framerate = 60
clock = pygame.time.Clock()

#---Screen assets---#
office_surface = pygame.Surface((680, 610))
office_surface.fill("Red")
upgrade_surface = pygame.Surface((490, 610))
upgrade_surface.fill("Blue")

#---Variables---#
   #--Fonts--#
value_font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 20)
upgrade_font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 16)

#---Functions---#


#---Game---#
while True:

#--Closing the window--#
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()  

#--Surfaces--#

   screen.blit(office_surface, (50, 50)) #--Office
   screen.blit(upgrade_surface, (740, 50)) #--Upgrade store

   pygame.display.update()
   clock.tick(framerate)  #limits FPS to 60
