from typing import List

import dearpygui.dearpygui as dpg
import pygame

from .colors import Colors
from .debug_window import DebugWindow
from .fluid_particle import FluidParticle
from .game_object import GameObject


class Game:
    debug: bool = False

    window: pygame.Surface
    screen: pygame.Surface

    game_objects: List[GameObject]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def init(window_width: int, window_height: int, fullscreen: bool) -> None:
        pygame.init()
        Game.window = pygame.display.set_mode((window_width, window_height))
        Game.screen = pygame.display.get_surface()

        if fullscreen != pygame.display.is_fullscreen():
            pygame.display.toggle_fullscreen()

        Game.game_objects = []

        particle_pos = pygame.Vector2(
            Game.screen.get_width() / 2, Game.screen.get_height() / 2
        )
        Game.game_objects.append(FluidParticle(particle_pos))

        if Game.debug:
            Game.game_objects.append(DebugWindow())

    def update(dt: float) -> None:
        for game_object in Game.game_objects:
            game_object.update(dt)

    def render() -> None:
        # render all game objects
        Game.window.fill(Colors.Black)
        for game_object in Game.game_objects:
            game_object.render(Game.screen)
        pygame.display.flip()

    def run() -> None:
        delta_clock: pygame.time.Clock = pygame.time.Clock()
        is_running: bool = True
        while is_running:
            dt: float = delta_clock.tick() / 1000

            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    is_running = False
            Game.update(dt)
            Game.render()

        for game_object in Game.game_objects:
            game_object.destroy()
        pygame.quit()
