import pygame

from .colors import Colors
from .vector2 import Vector2
from .game_object import GameObject
from .math_utils import sign
from .simulation_params import SimulationParams


class FluidParticle(GameObject):
    position: Vector2
    velocity: Vector2

    def __init__(self, position: Vector2) -> None:
        super().__init__()
        self.position = position
        self.velocity = Vector2.zero

    def update(self, dt: float) -> None:
        self.velocity += Vector2.down * SimulationParams.gravity * dt
        self.position += self.velocity * dt
        self.resolve_collisions()

    def render(self, screen) -> None:
        pygame.draw.circle(
            screen, Colors.LightBlue, self.position, SimulationParams.particle_radius
        )

    def resolve_collisions(self) -> None:
        half_bounds_size: Vector2 = (
            SimulationParams.get_bounds() / 2
            - Vector2.one * SimulationParams.particle_radius
        )

        if abs(self.position.x) > half_bounds_size.x:
            self.position.x = half_bounds_size.x * sign(self.position.x)
            self.velocity.x *= -1 * SimulationParams.collision_dampening

        if abs(self.position.y) > half_bounds_size.y:
            self.position.y = half_bounds_size.y * sign(self.position.y)
            self.velocity.y *= -1 * SimulationParams.collision_dampening
