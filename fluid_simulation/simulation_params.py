import pygame

from .vector2 import Vector2


class SimulationParams:
    particle_count: int = 10
    particle_spacing: float = 10.0

    particle_radius: float = 10.0
    gravity: float = 9.8
    bounds_size: Vector2 = Vector2(500, 500)
    collision_dampening: float = 1.0

    def get_bounds():
        return pygame.display.get_surface().get_size() + SimulationParams.bounds_size
