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
value_title_font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 20)
value_font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 25)
upgrade_font = pygame.font.Font("graphic/font/GoldenAgeShad.ttf", 17)

   #--Values--#
currency = 0
earn_value = 1

   #--Parameters--#
monitor_clicked = False


#---Functions---#

def draw_upgrade(x_pos, y_pos, height, width):
   border = pygame.rect.Rect(x_pos, y_pos, width, height)
   padding = pygame.rect.Rect(x_pos + 5, y_pos + 5, width - 10, height - 10)
   pygame.draw.rect(upgrade_surface, "Brown", border)
   pygame.draw.rect(upgrade_surface, "Black", padding)

def draw_counter(x_pos, y_pos, height, width):
   border = pygame.rect.Rect(y_pos, x_pos, width, height)
   padding = pygame.rect.Rect(y_pos + 5, x_pos + 5, width - 10, height - 10)
   pygame.draw.rect(upgrade_surface, "Brown", border)
   pygame.draw.rect(upgrade_surface, "Black", padding)

def draw_monitor(x_pos, y_pos):
   monitor = pygame.rect.Rect((x_pos, y_pos), (200, 170))
   pygame.draw.rect(office_surface, "Blue", monitor)

#---Game---#
while True:


   for event in pygame.event.get():
      if event.type == pygame.QUIT: #--Closing the window--#
        pygame.quit()
        exit()

      monitor_hitbox = pygame.rect.Rect((50 + 150, 50 + 300), (200, 170))


      #--Monitor clicking function--#
      if event.type == pygame.MOUSEBUTTONDOWN and monitor_clicked == False:
         if monitor_hitbox.collidepoint(event.pos):
            currency += earn_value
            monitor_clicked = True
      elif event.type == pygame.MOUSEBUTTONUP and monitor_clicked == True:
         time.sleep(0.05)
         monitor_clicked = False

      

#--Surfaces--#

   screen.blit(office_surface, (50, 50))
   screen.blit(upgrade_surface, (740, 50))

#--Monitor--#
   monitor = draw_monitor(150, 300)


#--Upgrade Window--#
   #--Paperclip counter--#
   draw_counter(5, 5, 120, 480)
   counter_text = value_title_font.render("Counter:", False, "White")
   screen.blit(counter_text, (760, 70))
   currency_text = value_font.render(f"{currency}", False, "White")
   screen.blit(currency_text, (800, 120))

   #--Upgrades--#
   computer = draw_upgrade(5, 160, 80, 480)
   desk = draw_upgrade(5, 280, 80, 480)
   decor = draw_upgrade(5, 400, 80, 480)
   boss = draw_upgrade(5, 515, 90, 480)

   pygame.display.update()
   clock.tick(framerate)  #limits FPS to 60
