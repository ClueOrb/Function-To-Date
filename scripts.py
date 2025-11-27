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
        monitor = pygame.image.load("graphic/PC.png")
        window.screen.blit(monitor, (x_pos, y_pos))

    def draw_desk(x_pos, y_pos):
        desk = pygame.image.load("graphic/Desk.png")
        window.screen.blit(desk, (x_pos, y_pos))

    def draw_boss(x_pos, y_pos):
        desk = pygame.image.load("graphic/Boss.png")
        window.screen.blit(desk, (x_pos, y_pos))

def exit():
        pygame.quit()
        exit()
