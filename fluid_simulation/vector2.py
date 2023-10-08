import pygame


class Vector2(pygame.Vector2):
    ZERO = pygame.Vector2(0, 0)
    RIGHT = pygame.Vector2(1, 0)
    LEFT = pygame.Vector2(-1, 0)
    UP = pygame.Vector2(0, -1)
    DOWN = pygame.Vector2(0, 1)
