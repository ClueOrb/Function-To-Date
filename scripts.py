import pygame
from sys import exit
from game_window import *
from variables import *

#--Draws buttons--#

class draw():

    def draw_upgrade(x_pos, y_pos, height, width):
        border = pygame.rect.Rect(x_pos, y_pos, width, height)
        padding = pygame.rect.Rect(x_pos + 5, y_pos + 5, width - 10, height - 10)
        pygame.draw.rect(game.upgrade_surface, "Brown", border)
        pygame.draw.rect(game.upgrade_surface, "Black", padding)

    def draw_counter(x_pos, y_pos, height, width):
        border = pygame.rect.Rect(y_pos, x_pos, width, height)
        padding = pygame.rect.Rect(y_pos + 5, x_pos + 5, width - 10, height - 10)
        pygame.draw.rect(game.upgrade_surface, "Brown", border)
        pygame.draw.rect(game.upgrade_surface, "Black", padding)

    def draw_monitor(x_pos, y_pos):
        monitor = pygame.image.load("graphic/assets/computer_lvl1.png")
        window.screen.blit(monitor, (x_pos, y_pos))

    def draw_table(x_pos, y_pos):
        desk = pygame.rect.Rect((x_pos, y_pos), (650, 250))
        pygame.draw.rect(game.office_surface, "Green", desk)

def exit():
        pygame.quit()
        exit()
