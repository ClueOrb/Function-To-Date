import pygame
from game_window import game

class hb():
    monitor_hb = pygame.rect.Rect((50 + 150, 50 + 300), (200, 170))
    #pygame.draw.rect(game.office_surface, "red", monitor_hb)

    pc_hb = pygame.rect.Rect((740 + 5, 50 + 160), (480, 80))
    #pygame.draw.rect(game.upgrade_surface, "blue", pc_hb)

    desk_hb = pygame.rect.Rect((740 + 5, 50 + 280), (480, 80))
    #pygame.draw.rect(game.upgrade_surface, "blue", desk_hb)

    decor_hb = pygame.rect.Rect((740 + 5, 50 + 400), (480, 80))
    #pygame.draw.rect(game.upgrade_surface, "blue", decor_hb)

    boss_hb = pygame.rect.Rect((740 + 5, 50 + 515), (480, 80))
    #pygame.draw.rect(game.upgrade_surface, "blue", boss_hb)