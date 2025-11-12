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


      #--Monitor clicking function--#
      monitor_hitbox = pygame.rect.Rect((50 + 150, 50 + 300), (200, 170))

      if event.type == pygame.MOUSEBUTTONDOWN and monitor_clicked == False:
         if monitor_hitbox.collidepoint(event.pos):
            currency += earn_value
            monitor_clicked = True
      elif event.type == pygame.MOUSEBUTTONUP and monitor_clicked == True:
         time.sleep(0.05)
         monitor_clicked = False

      #--Computer Upgrade--#
      computer_hitbox = pygame.rect.Rect((740 + 5, 50 + 160), (480, 80))
      
      if event.type == pygame.MOUSEBUTTONDOWN and currency >= computer_req:
         if computer_hitbox.collidepoint(event.pos):
            if currency >= computer_req and computer_lvl == 1:  # Level 1 → 2
               currency -= computer_req
               computer_req = 1000
               computer_lvl += 1
               earn_value += 1
            elif currency >= computer_req and computer_lvl == 2:  # Level 2 → 3
               currency -= computer_req
               computer_req = 1500
               computer_lvl += 1
               earn_value += 2
            elif currency >= computer_req and computer_lvl == 3:  # Level 3 → 4
               currency -= computer_req
               computer_req = 2000
               computer_lvl += 1
               earn_value += 3
            elif currency >= computer_req and computer_lvl == 4:  # Level 4 → 5
               currency -= computer_req
               computer_lvl = "MAX"
               earn_value += 5

      #--Desk Upgrade--#
      desk_hitbox = pygame.rect.Rect((740 + 5, 50 + 280), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and currency >= desk_req:
         if desk_hitbox.collidepoint(event.pos):
            if currency >= desk_req and desk_lvl == 1:  # Level 1 → 2
               currency -= desk_req
               desk_req = 500
               desk_lvl += 1
               earn_value += 1
            elif currency >= desk_req and desk_lvl == 2:  # Level 2 → 3
               currency -= desk_req
               desk_req = 1000
               desk_lvl += 1
               earn_value += 1
            elif currency >= desk_req and desk_lvl == 3:  # Level 3 → 4
               currency -= desk_req
               desk_req = 1500
               desk_lvl += 1
               earn_value += 2
            elif currency >= desk_req and desk_lvl == 4:  # Level 4 → 5
               currency -= desk_req
               desk_lvl = "MAX"
               earn_value += 4

      #--Decor Upgrade--#
      decor_hitbox = pygame.rect.Rect((740 + 5, 50 + 400), (480, 80))

      if event.type == pygame.MOUSEBUTTONDOWN and currency >= decor_req:
         if decor_hitbox.collidepoint(event.pos):
            if currency >= decor_req and decor_lvl == 1:  # Level 1 → 2
               currency -= decor_req
               decor_req = 150
               decor_lvl += 1
               earn_value += 1
            elif currency >= decor_req and decor_lvl == 2:  # Level 2 → 3
               currency -= decor_req
               decor_req = 200
               decor_lvl += 1
               earn_value += 1
            elif currency >= decor_req and decor_lvl == 3:  # Level 3 → 4
               currency -= decor_req
               decor_req = 800
               decor_lvl += 1
               earn_value += 2
            elif currency >= decor_req and decor_lvl == 4:  # Level 4 → 5
               currency -= decor_req
               decor_lvl = "MAX"
               earn_value += 2
            

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
      #--Computer--#
   computer = draw_upgrade(5, 160, 80, 480)
   computer_up_text = upgrade_font.render(f"Computer lvl: {computer_lvl}", False, "White")
   if computer_lvl == "MAX":
      computer_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      computer_req_text = upgrade_font.render(f"Upgrade: {computer_req}", False, "White")
   screen.blit(computer_up_text, (760, 225))
   screen.blit(computer_req_text, (1045, 265))

      #--Desk--#
   desk = draw_upgrade(5, 280, 80, 480)
   desk_up_text = upgrade_font.render(f"Desk lvl: {desk_lvl}", False, "White")
   if desk_lvl == "MAX":
      desk_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      desk_req_text = upgrade_font.render(f"Upgrade: {desk_req}", False, "White")
   screen.blit(desk_up_text, (760, 345))
   screen.blit(desk_req_text, (1045, 385))

      #--Decor--#
   decor = draw_upgrade(5, 400, 80, 480)
   decor_up_text = upgrade_font.render(f"Decor lvl: {decor_lvl}", False, "White")
   if decor_lvl == "MAX":
      decor_req_text = upgrade_font.render(f"Fully upgraded", False, "White")
   else:
      decor_req_text = upgrade_font.render(f"Upgrade: {decor_req}", False, "White")
   screen.blit(decor_up_text, (760, 465))
   screen.blit(decor_req_text, (1045, 505))

   boss = draw_upgrade(5, 515, 90, 480)

   pygame.display.update()
   clock.tick(framerate)  #limits FPS to 60
