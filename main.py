import pygame
import time
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
font = pygame.font.Font("freesansbold.ttf", 16)

#variables
monitor_value = 0
monitor_clicked = False

#functions
def draw_monitor():
   monitor = pygame.Rect(250, 250, 200, 170)
   pygame.draw.rect(test_surface, "Blue", monitor)
   return monitor

while True:

#Closing the window
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    monitor_hitbox = pygame.Rect(60 + 250, 60 + 250, 200, 170)

    if event.type == pygame.MOUSEBUTTONDOWN and monitor_clicked == False:
       if monitor_hitbox.collidepoint(event.pos):
          monitor_value += 1
          monitor_clicked = True
    elif event.type == pygame.MOUSEBUTTONUP and monitor_clicked == True:
          time.sleep(0.05)
          monitor_clicked = False
          

    screen.blit(background,(0, 0)) #Draws game screen
    screen.blit(test_surface,(60, 60)) #Draws game window
    monitor = draw_monitor() #Draws monitor
    paperclips = font.render(f"Paperclips: {monitor_value}", 16, "White")
    screen.blit(paperclips, (1000, 20))

    pygame.display.update()
    clock.tick(framerate)  # limits FPS to 60
