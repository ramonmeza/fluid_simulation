import pygame

from .colors import Colors
from .vector2 import Vector2
from .game_object import GameObject
from .simulation_params import SimulationParams


class FluidParticle(GameObject):
    position: Vector2
    velocity: Vector2

    def __init__(self, position: Vector2) -> None:
        super().__init__()
        self.position = position
        self.velocity = Vector2.ZERO

    def update(self, dt: float) -> None:
        self.velocity += Vector2.DOWN * SimulationParams.gravity * dt
        self.position += self.velocity * dt

    def render(self, screen) -> None:
        pygame.draw.circle(
            screen, Colors.LightBlue, self.position, SimulationParams.particle_radius
        )
