import pygame
from sys import exit
from gameWindow import MainSetUp
from gameWindow import GameWindow
from variables import Values
from functions import draw
from fonts import Font

#----Initialize Pygame----#
pygame.init()

#---Game---#
while True:


   for event in pygame.event.get():
      if event.type == pygame.QUIT: #--Closing the window--#
        pygame.quit()
        exit()

      #--Monitor clicking function--#
      monitor_hitbox = pygame.rect.Rect((50 + 150, 50 + 300), (200, 170))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and monitor_hitbox.collidepoint(event.pos):
         Values.currency += Values.earn_value

      #--Computer Upgrade--#
      computer_hitbox = pygame.rect.Rect((740 + 5, 50 + 160), (480, 80))
      
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and  computer_hitbox.collidepoint(event.pos) and Values.currency >= Values.computer_req:
         computer_progress = {
            1: (1000, 1),
            2: (2000, 1),
            3: (4000, 2),
            4: (0, 4),
         }

         if isinstance(Values.computer_lvl, int) and Values.computer_lvl in computer_progress:
            Values.currency -= Values.computer_req
            next_req, gain = computer_progress[Values.computer_lvl]
            earn_value += gain
            if Values.computer_lvl == 4:
               Values.computer_lvl = "MAX"
               Values.computer_req = 0
            else:
               Values.computer_lvl += 1
               Values.computer_req = next_req



      #--Desk Upgrade--#
      desk_hitbox = pygame.rect.Rect((740 + 5, 50 + 280), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and desk_hitbox.collidepoint(event.pos) and Values.currency >= Values.desk_req:
         desk_progress = {
            1: (500, 1),
            2: (750, 1),
            3: (1500, 1),
            4: (0, 2),
         }

         if isinstance(Values.desk_lvl, int) and Values.desk_lvl in desk_progress:
            Values.currency -= Values.desk_req
            next_req, gain = desk_progress[Values.desk_lvl]
            earn_value += gain
            if Values.desk_lvl == 4:
               Values.desk_lvl = "MAX"
               Values.desk_req = 0
            else:
               Values.desk_lvl += 1
               Values.desk_req = next_req

      #--Decor Upgrade--#
      decor_hitbox = pygame.rect.Rect((740 + 5, 50 + 400), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and decor_hitbox.collidepoint(event.pos) and Values.currency >= Values.decor_req:
         decor_progress = {
            1: (200, 1),
            2: (400, 1),
            3: (600, 1),
            4: (0, 1),
         }

         if isinstance(Values.decor_lvl, int) and Values.decor_lvl in decor_progress:
            Values.currency -= Values.decor_req
            next_req, gain = decor_progress[Values.decor_lvl]
            Values.earn_value += gain
            if Values.decor_lvl == 4:
               Values.decor_lvl = "MAX"
               Values.decor_req = 0
            else:
               Values.decor_lvl += 1
               Values.decor_req = next_req

      #--Boss Upgrade--#
      boss_hitbox = pygame.rect.Rect((740 + 5, 50 + 515), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and boss_hitbox.collidepoint(event.pos) and Values.currency >= Values.boss_req:
         boss_progress = {
            1: (2000, 1),
            2: (5000, 3),
            3: (20000, 4),
            4: (0, 5),
         }

         if isinstance(Values.boss_lvl, int) and Values.boss_lvl in boss_progress:
            Values.currency -= Values.boss_req
            next_req, gain = boss_progress[Values.boss_lvl]
            Values.earn_value += gain
            if Values.boss_lvl == 4:
               Values.boss_lvl = "MAX"
               Values.boss_req = 0
            else:
               Values.boss_lvl += 1
               Values.boss_req = next_req

            

#--Surfaces--#

   MainSetUp.screen.blit(GameWindow.game_background, (0, 0))
   MainSetUp.screen.blit(GameWindow.office_surface, (50, 50))
   MainSetUp.screen.blit(GameWindow.upgrade_surface, (740, 50))
#--Table--#
   table = draw.draw_table(15, 400)

#--Monitor--#
   monitor = draw.draw_monitor(200, 340)

#--Upgrade Window--#
   #--Paperclip counter--#
   draw.draw_counter(5, 5, 120, 480)
   counter_text = Font.value_title_font.render("Counter:", False, "White")
   MainSetUp.screen.blit(counter_text, (760, 70))
   currency_text = Font.value_font.render(f"{Values.currency}", False, "White")
   MainSetUp.screen.blit(currency_text, (800, 120))

   #--Upgrades--#
      #--Computer--#
   computer = draw.draw_upgrade(5, 160, 80, 480)
   computer_up_text = Font.upgrade_font.render(f"Computer lvl: {Values.computer_lvl}", False, "White")
   if Values.computer_lvl == "MAX":
      computer_req_text = Font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      computer_req_text = Font.upgrade_font.render(f"Upgrade: {Values.computer_req}", False, "White")
   MainSetUp.screen.blit(computer_up_text, (760, 225))
   MainSetUp.screen.blit(computer_req_text, (1045, 265))

      #--Desk--#
   desk = draw.draw_upgrade(5, 280, 80, 480)
   desk_up_text = Font.upgrade_font.render(f"Desk lvl: {Values.desk_lvl}", False, "White")
   if Values.desk_lvl == "MAX":
      desk_req_text = Font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      desk_req_text = Font.upgrade_font.render(f"Upgrade: {Values.desk_req}", False, "White")
   MainSetUp.screen.blit(desk_up_text, (760, 345))
   MainSetUp.screen.blit(desk_req_text, (1045, 385))

      #--Decor--#
   decor = draw.draw_upgrade(5, 400, 80, 480)
   decor_up_text = Font.upgrade_font.render(f"Decor lvl: {Values.decor_lvl}", False, "White")
   if Values.decor_lvl == "MAX":
      decor_req_text = Font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      decor_req_text = Font.upgrade_font.render(f"Upgrade: {Values.decor_req}", False, "White")
   MainSetUp.screen.blit(decor_up_text, (760, 465))
   MainSetUp.screen.blit(decor_req_text, (1045, 505))

   boss = draw.draw_upgrade(5, 515, 90, 480)
   boss_up_text = Font.upgrade_font.render(f"Boss lvl: {Values.boss_lvl}", False, "White")
   if Values.boss_lvl == "MAX":
      boss_req_text = Font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      boss_req_text = Font.upgrade_font.render(f"Upgrade: {Values.boss_req}", False, "White")
   MainSetUp.screen.blit(boss_up_text, (760, 580))
   MainSetUp.screen.blit(boss_req_text, (1045, 630))

   pygame.display.update()
   MainSetUp.clock.tick(Values.framerate)  #limits FPS to 60
