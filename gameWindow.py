import pygame

#---Main set up (Screen, Title)---#
class MainSetUp():

    screen = pygame.display.set_mode((1280, 720), 0)
    pygame.display.set_caption('Function to Date')
    icon = pygame.image.load("graphic/icon.png")
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

class GameWindow():
    #---Screen assets---#
    game_background = pygame.image.load("graphic/assets/mainbg.png")
    office_surface = pygame.Surface((680, 610))
    office_surface.fill("White")
    upgrade_surface = pygame.Surface((490, 610))
    upgrade_surface.fill("Red")