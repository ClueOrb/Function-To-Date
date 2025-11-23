import pygame
from sys import exit
from gameWindow import MainSetUp
from gameWindow import GameWindow
from variables import Values
from functions import draw

#----Initialize Pygame----#
pygame.init()

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

   #--Levels--#
computer_lvl = 1
desk_lvl = 1
decor_lvl = 1
boss_lvl = 1

   #--Level up requirement--#
computer_req = 500
desk_req = 250
decor_req = 100
boss_req = 1000

#---Functions---#

def draw_counter(x_pos, y_pos, height, width):
   border = pygame.rect.Rect(y_pos, x_pos, width, height)
   padding = pygame.rect.Rect(y_pos + 5, x_pos + 5, width - 10, height - 10)
   pygame.draw.rect(GameWindow.upgrade_surface, "Brown", border)
   pygame.draw.rect(GameWindow.upgrade_surface, "Black", padding)

def draw_monitor(x_pos, y_pos):
   monitor = pygame.image.load("graphic/assets/computer_lvl1.png")
   MainSetUp.screen.blit(monitor, (x_pos, y_pos))

def draw_table(x_pos, y_pos):
   desk = pygame.rect.Rect((x_pos, y_pos), (650, 250))
   pygame.draw.rect(GameWindow.office_surface, "Green", desk)

#---Game---#
while True:


   for event in pygame.event.get():
      if event.type == pygame.QUIT: #--Closing the window--#
        pygame.quit()
        exit()


      #--Monitor clicking function--#
      monitor_hitbox = pygame.rect.Rect((50 + 150, 50 + 300), (200, 170))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and monitor_hitbox.collidepoint(event.pos):
         currency += earn_value

      #--Computer Upgrade--#
      computer_hitbox = pygame.rect.Rect((740 + 5, 50 + 160), (480, 80))
      
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and  computer_hitbox.collidepoint(event.pos) and currency >= computer_req:
         computer_progress = {
            1: (1000, 1),
            2: (2000, 1),
            3: (4000, 2),
            4: (0, 4),
         }

         if isinstance(computer_lvl, int) and computer_lvl in computer_progress:
            currency -= computer_req
            next_req, gain = computer_progress[computer_lvl]
            earn_value += gain
            if computer_lvl == 4:
               computer_lvl = "MAX"
               computer_req = 0
            else:
               computer_lvl += 1
               computer_req = next_req



      #--Desk Upgrade--#
      desk_hitbox = pygame.rect.Rect((740 + 5, 50 + 280), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and desk_hitbox.collidepoint(event.pos) and currency >= desk_req:
         desk_progress = {
            1: (500, 1),
            2: (750, 1),
            3: (1500, 1),
            4: (0, 2),
         }

         if isinstance(desk_lvl, int) and desk_lvl in desk_progress:
            currency -= desk_req
            next_req, gain = desk_progress[desk_lvl]
            earn_value += gain
            if desk_lvl == 4:
               desk_lvl = "MAX"
               desk_req = 0
            else:
               desk_lvl += 1
               desk_req = next_req

      #--Decor Upgrade--#
      decor_hitbox = pygame.rect.Rect((740 + 5, 50 + 400), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and decor_hitbox.collidepoint(event.pos) and currency >= decor_req:
         decor_progress = {
            1: (200, 1),
            2: (400, 1),
            3: (600, 1),
            4: (0, 1),
         }

         if isinstance(decor_lvl, int) and decor_lvl in decor_progress:
            currency -= decor_req
            next_req, gain = decor_progress[decor_lvl]
            earn_value += gain
            if decor_lvl == 4:
               decor_lvl = "MAX"
               decor_req = 0
            else:
               decor_lvl += 1
               decor_req = next_req

      #--Boss Upgrade--#
      boss_hitbox = pygame.rect.Rect((740 + 5, 50 + 515), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and boss_hitbox.collidepoint(event.pos) and currency >= boss_req:
         boss_progress = {
            1: (2000, 1),
            2: (5000, 3),
            3: (20000, 4),
            4: (0, 5),
         }

         if isinstance(boss_lvl, int) and boss_lvl in boss_progress:
            currency -= boss_req
            next_req, gain = boss_progress[boss_lvl]
            earn_value += gain
            if boss_lvl == 4:
               boss_lvl = "MAX"
               boss_req = 0
            else:
               boss_lvl += 1
               boss_req = next_req

            

#--Surfaces--#

   MainSetUp.screen.blit(GameWindow.game_background, (0, 0))
   MainSetUp.screen.blit(GameWindow.office_surface, (50, 50))
   MainSetUp.screen.blit(GameWindow.upgrade_surface, (740, 50))
#--Table--#
   table = draw_table(15, 400)

#--Monitor--#
   monitor = draw_monitor(200, 340)

#--Upgrade Window--#
   #--Paperclip counter--#
   draw_counter(5, 5, 120, 480)
   counter_text = value_title_font.render("Counter:", False, "White")
   MainSetUp.screen.blit(counter_text, (760, 70))
   currency_text = value_font.render(f"{currency}", False, "White")
   MainSetUp.screen.blit(currency_text, (800, 120))

   #--Upgrades--#
      #--Computer--#
   computer = draw.draw_upgrade(5, 160, 80, 480)
   computer_up_text = upgrade_font.render(f"Computer lvl: {computer_lvl}", False, "White")
   if computer_lvl == "MAX":
      computer_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      computer_req_text = upgrade_font.render(f"Upgrade: {computer_req}", False, "White")
   MainSetUp.screen.blit(computer_up_text, (760, 225))
   MainSetUp.screen.blit(computer_req_text, (1045, 265))

      #--Desk--#
   desk = draw.draw_upgrade(5, 280, 80, 480)
   desk_up_text = upgrade_font.render(f"Desk lvl: {desk_lvl}", False, "White")
   if desk_lvl == "MAX":
      desk_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      desk_req_text = upgrade_font.render(f"Upgrade: {desk_req}", False, "White")
   MainSetUp.screen.blit(desk_up_text, (760, 345))
   MainSetUp.screen.blit(desk_req_text, (1045, 385))

      #--Decor--#
   decor = draw.draw_upgrade(5, 400, 80, 480)
   decor_up_text = upgrade_font.render(f"Decor lvl: {decor_lvl}", False, "White")
   if decor_lvl == "MAX":
      decor_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      decor_req_text = upgrade_font.render(f"Upgrade: {decor_req}", False, "White")
   MainSetUp.screen.blit(decor_up_text, (760, 465))
   MainSetUp.screen.blit(decor_req_text, (1045, 505))

   boss = draw.draw_upgrade(5, 515, 90, 480)
   boss_up_text = upgrade_font.render(f"Boss lvl: {boss_lvl}", False, "White")
   if boss_lvl == "MAX":
      boss_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      boss_req_text = upgrade_font.render(f"Upgrade: {boss_req}", False, "White")
   MainSetUp.screen.blit(boss_up_text, (760, 580))
   MainSetUp.screen.blit(boss_req_text, (1045, 630))

   pygame.display.update()
   MainSetUp.clock.tick(Values.framerate)  #limits FPS to 60
