from typing import List

import pygame

from .colors import Colors
from .game_object import GameObject


class Game:
    window: pygame.Surface
    screen: pygame.Surface
    
    game_objects: List[GameObject]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def init(window_width: int, window_height: int, fullscreen: bool) -> None:
        pygame.init()
        Game.window = pygame.display.set_mode((window_width, window_height))
        Game.screen = pygame.display.get_surface()
        
        if fullscreen != pygame.display.is_fullscreen():
            pygame.display.toggle_fullscreen()
        
        Game.game_objects = []
        
    def update(dt: float) -> None:
        print(dt)
    
    def render() -> None:
        Game.window.fill(Colors.Black)
        pygame.display.flip()

    def run() -> None:
        delta_clock: pygame.time.Clock = pygame.time.Clock()
        is_running: bool = True
        while is_running:
            dt: float = delta_clock.tick()
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    is_running = False
            Game.update(dt)
            Game.render()
