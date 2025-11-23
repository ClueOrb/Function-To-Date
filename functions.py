import pygame
from gameWindow import GameWindow
class draw():

    def __init__(self):
        self.draw_upgrade()

    def draw_upgrade(x_pos, y_pos, height, width):
        border = pygame.rect.Rect(x_pos, y_pos, width, height)
        padding = pygame.rect.Rect(x_pos + 5, y_pos + 5, width - 10, height - 10)
        pygame.draw.rect(GameWindow.upgrade_surface, "Brown", border)
        pygame.draw.rect(GameWindow.upgrade_surface, "Black", padding)