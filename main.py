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
font_placeholder = pygame.font.Font("freesansbold.ttf", 15)
font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 15)

#variables
paperclips = 0
monitor_clicked = False
current_value = 1

#for upgrades
setup_lvl = 1
desk_lvl = 1
decor_lvl = 1
boss_lvl = 1

#for display
dis_setup_lvl = 1
dis_desk_lvl = 1
dis_decor_lvl = 1
dis_boss_lvl = 1

setup_req = 25
desk_req = 10
decor_req = 5
boss_req = 100

#display variables
upgrade_x = 820



#functions
def draw_monitor():
   monitor = pygame.Rect(250, 250, 200, 170)
   pygame.draw.rect(test_surface, "Blue", monitor)
   return monitor

def draw_money(x_const, y_const):
   money_frame = pygame.Rect(x_const, y_const, 450, 100)
   money_frame_black = pygame.Rect(x_const + 10, y_const + 10, 430, 80)
   pygame.draw.rect(screen, "Brown", money_frame)
   pygame.draw.rect(screen, "Black", money_frame_black)

def draw_upgrade(x_const, y_const):
   upgrade_frame = pygame.Rect(x_const, y_const, 450, 80)
   upgrade_frame_black = pygame.Rect(x_const + 5, y_const + 5, 440, 70)
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

      if event.type == pygame.MOUSEBUTTONDOWN and monitor_clicked == False: #If mouse is clicked
         if monitor.collidepoint(event.pos):
            paperclips += current_value
            monitor_clicked = True
      elif event.type == pygame.MOUSEBUTTONUP and monitor_clicked == True: #If mouse is released
         time.sleep(0.05)
         monitor_clicked = False

      desk_hitbox = pygame.Rect(800, 180, 450, 100)

      if event.type == pygame.MOUSEBUTTONDOWN:
         if desk_hitbox.collidepoint(event.pos):
            if paperclips >= desk_req and desk_lvl < 5:
               desk_lvl += 1
               paperclips -= desk_req

   screen.blit(background,(0, 0)) #Draws game screen
   screen.blit(test_surface,(60, 60)) #Draws game window
   monitor = draw_monitor() #Draws monitor


   draw_money(800, 55)
   paperclips_text = font.render(f"Paperclips: {paperclips}", 0, "White") #Renders the font and text
   screen.blit(paperclips_text, (890, 100)) #Draws the text and current 


   #Desk
   draw_upgrade(800, 180)
   desk_up_text = font.render(f"Desk level: {desk_lvl}", 0, "White") 
   screen.blit(desk_up_text, (upgrade_x, 215))

   #Computer set up
   draw_upgrade(800, 280)
   computer_up_text = font.render(f"Computer level: {setup_lvl}", 0, "White") 
   screen.blit(computer_up_text, (upgrade_x, 315)) 

   #Desk Decor
   draw_upgrade(800, 380)
   decor_up_text = font.render(f"Desk asseccory level: {decor_lvl}", 0, "White") 
   screen.blit(decor_up_text, (upgrade_x, 415)) 

   #Boss
   draw_upgrade(800, 600)
   decor_up_text = font.render(f"Boss affection: {decor_lvl}", 0, "White") 
   screen.blit(decor_up_text, (upgrade_x, 635)) 

   pygame.display.update()
   clock.tick(framerate)  # limits FPS to 60