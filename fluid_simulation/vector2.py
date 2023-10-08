import pygame


class Vector2(pygame.Vector2):
    zero = pygame.Vector2(0, 0)
    one = pygame.Vector2(1, 1)
    right = pygame.Vector2(1, 0)
    left = pygame.Vector2(-1, 0)
    up = pygame.Vector2(0, -1)
    down = pygame.Vector2(0, 1)
