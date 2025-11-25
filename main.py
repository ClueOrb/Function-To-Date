import pygame
from scripts import *
from hitboxes import hb
from variables import *
from game_window import *
from fonts import font
#----Initialize Pygame----#
pygame.init()

#---Game---#
while True:


   for event in pygame.event.get():
      if event.type == pygame.QUIT: #--Close the game--#
         exit()

      #--Monitor clicking function--#
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and hb.monitor_hb.collidepoint(event.pos): #--Checking if left mouse button gets pressed on the monitor hitbox--#
         base.currency += base.earn_value

      #--Computer Upgrade--#
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and hb.pc_hb.collidepoint(event.pos) and base.currency >= cost.pc_req:
         computer_progress = {
            1: (1000, 1),
            2: (2000, 1),
            3: (4000, 2),
            4: (0, 4),
         }

         if isinstance(level.pc_lvl, int) and level.pc_lvl in computer_progress:
            base.currency -= cost.pc_req
            next_req, gain = computer_progress[level.pc_lvl]
            base.earn_value += gain
            if level.pc_lvl == 4:
                  level.pc_lvl = "MAX"
                  cost.pc_req = 0
            else:
                  level.pc_lvl += 1
                  cost.pc_req = next_req


      #--Desk Upgrade--#
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and hb.desk_hb.collidepoint(event.pos) and base.currency >= cost.desk_req:
         desk_progress = {
            1: (500, 1),
            2: (750, 1),
            3: (1500, 1),
            4: (0, 2),
         }

         if isinstance(level.desk_lvl, int) and level.desk_lvl in desk_progress:
            base.currency -= cost.desk_req
            next_req, gain = desk_progress[level.desk_lvl]
            base.earn_value += gain
            if level.desk_lvl == 4:
               level.desk_lvl = "MAX"
               cost.desk_req = 0
            else:
               level.desk_lvl += 1
               cost.desk_req = next_req

      #--Decor Upgrade--#
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and hb.decor_hb.collidepoint(event.pos) and base.currency >= cost.decor_req:
         decor_progress = {
                  1: (200, 1),
                  2: (400, 1),
                  3: (600, 1),
                  4: (0, 1),
            }

         if isinstance(level.decor_lvl, int) and level.decor_lvl in decor_progress:
            base.currency -= cost.decor_req
            next_req, gain = decor_progress[level.decor_lvl]
            base.earn_value += gain
            if level.decor_lvl == 4:
               level.decor_lvl = "MAX"
               cost.decor_req = 0
            else:
               level.decor_lvl += 1
               cost.decor_req = next_req

      #--Boss Upgrade--#
      if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and hb.boss_hb.collidepoint(event.pos) and base.currency >= cost.boss_req:
         boss_progress = {
            1: (2000, 1),
            2: (5000, 3),
            3: (20000, 4),
            4: (0, 5),
         }

         if isinstance(level.boss_lvl, int) and level.boss_lvl in boss_progress:
            base.currency -= cost.boss_req
            next_req, gain = boss_progress[level.boss_lvl]
            base.earn_value += gain
         if level.boss_lvl == 4:
               level.boss_lvl = "MAX"
               cost.boss_req = 0
         else:
               level.boss_lvl += 1
               cost.boss_req = next_req

            

#--Surfaces--#

   window.screen.blit(game.game_background, (0, 0))
   window.screen.blit(game.office_surface, (50, 50))
   window.screen.blit(game.upgrade_surface, (740, 50))


#--Table--#

   draw.draw_table(15, 400)

#--Monitor--#

   draw.draw_monitor(200, 340)

#--Upgrade Window--#
   #--Paperclip counter--#
   draw.draw_counter(5, 5, 120, 480)
   counter_text = font.value_title_font.render("Counter:", False, "White")
   window.screen.blit(counter_text, (760, 70))
   currency_text = font.value_font.render(f"{base.currency}", False, "White")
   window.screen.blit(currency_text, (800, 120))

   #--Upgrade buttons--#
      #--Computer--#
   draw.draw_upgrade(5, 160, 80, 480)
   computer_up_text = font.upgrade_font.render(f"Computer lvl: {level.pc_lvl}", False, "White")
   if level.pc_lvl == "MAX":
      computer_req_text = font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      computer_req_text = font.upgrade_font.render(f"Upgrade: {cost.pc_req}", False, "White")
   window.screen.blit(computer_up_text, (760, 225))
   window.screen.blit(computer_req_text, (1045, 265))

      #--Desk--#
   draw.draw_upgrade(5, 280, 80, 480)
   desk_up_text = font.upgrade_font.render(f"Desk lvl: {level.desk_lvl}", False, "White")
   if level.desk_lvl == "MAX":
      desk_req_text = font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      desk_req_text = font.upgrade_font.render(f"Upgrade: {cost.desk_req}", False, "White")
   window.screen.blit(desk_up_text, (760, 345))
   window.screen.blit(desk_req_text, (1045, 385))

      #--Decor--#
   draw.draw_upgrade(5, 400, 80, 480)
   decor_up_text = font.upgrade_font.render(f"Decor lvl: {level.decor_lvl}", False, "White")
   if level.decor_lvl == "MAX":
      decor_req_text = font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      decor_req_text = font.upgrade_font.render(f"Upgrade: {cost.decor_req}", False, "White")
   window.screen.blit(decor_up_text, (760, 465))
   window.screen.blit(decor_req_text, (1045, 505)) 

      #--Boss__#
   draw.draw_upgrade(5, 515, 90, 480)
   boss_up_text = font.upgrade_font.render(f"Boss lvl: {level.boss_lvl}", False, "White")
   if level.boss_lvl == "MAX":
      boss_req_text = font.upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      boss_req_text = font.upgrade_font.render(f"Upgrade: {cost.boss_req}", False, "White")
   window.screen.blit(boss_up_text, (760, 580))
   window.screen.blit(boss_req_text, (1045, 630))

   pygame.display.update()
   window.clock.tick(base.framerate)  #limits FPS to 60
