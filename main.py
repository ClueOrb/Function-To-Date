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
font_placeholder = pygame.font.Font("freesansbold.ttf", 18)
font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 18)

#variables
paperclips = 0
monitor_clicked = False
setup_lvl = 1
desk_lvl = 1
decor_lvl = 1
boss_lvl = 1
current_value = 1

#functions
def draw_monitor():
   monitor = pygame.Rect(250, 250, 200, 170)
   pygame.draw.rect(test_surface, "Blue", monitor)
   return monitor

def draw_moneyboarder(x_const, y_const):
   money_frame = pygame.Rect(x_const, y_const, 380, 100)
   money_frame_black = pygame.Rect(x_const + 10, y_const + 10, 360, 80)
   pygame.draw.rect(screen, "Brown", money_frame)
   pygame.draw.rect(screen, "Black", money_frame_black)

def draw_upgrade(x_const, y_const):
   upgrade_frame = pygame.Rect(x_const, y_const, 380, 80)
   upgrade_frame_black = pygame.Rect(x_const + 5, y_const + 5, 370, 70)
   pygame.draw.rect(screen, "Brown", upgrade_frame)
   pygame.draw.rect(screen, "Black", upgrade_frame_black)

#Game
while True:

#Closing the window
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        exit()

   monitor_hitbox = pygame.Rect(60 + 250, 60 + 250, 200, 170)

   if event.type == pygame.MOUSEBUTTONDOWN and monitor_clicked == False:
       if monitor_hitbox.collidepoint(event.pos):
          paperclips += current_value
          monitor_clicked = True
   elif event.type == pygame.MOUSEBUTTONUP and monitor_clicked == True:
          time.sleep(0.05)
          monitor_clicked = False
          

   screen.blit(background,(0, 0)) #Draws game screen
   screen.blit(test_surface,(60, 60)) #Draws game window
   monitor = draw_monitor() #Draws monitor

   draw_moneyboarder(850, 55)
   paperclips_text = font.render(f"Paperclips: {paperclips}", 0, "White") #Renders the font and text
   screen.blit(paperclips_text, (890, 100)) #Draws the text and current 

   draw_upgrade(850, 180)
   draw_upgrade(850, 280)
   draw_upgrade(850, 380)
   draw_upgrade(850, 500)

   pygame.display.update()
   clock.tick(framerate)  # limits FPS to 60
