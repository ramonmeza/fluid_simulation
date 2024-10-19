import math
from typing import List


import pygame

from .colors import Colors
from .vector2 import Vector2
from .game_object import GameObject
from .math_utils import sign
from .simulation_params import SimulationParams


class FluidParticle(GameObject):
    positions: List[Vector2]
    velocities: List[Vector2]

    def __init__(self, position: Vector2) -> None:
        super().__init__()
        self.positions = [Vector2.zero] * SimulationParams.particle_count
        self.velocities = [Vector2.zero] * SimulationParams.particle_count
        
        particles_per_row = int(math.sqrt(SimulationParams.particle_count))
        particles_per_col = (SimulationParams.particle_count - 1) / particles_per_row + 1
        spacing = SimulationParams.particle_radius * 2 + SimulationParams.particle_spacing
        
        for i in range(SimulationParams.particle_count):
            x = (i % particles_per_row - particles_per_row / 2 + 0.5) * spacing
            y = (i / particles_per_row - particles_per_col / 2 + 0.5) * spacing
            self.positions[i] = position + Vector2(x, y)

    def update(self, dt: float) -> None:
        for i in range(len(self.positions)):
            self.velocities[i] += Vector2.down * SimulationParams.gravity * dt
            self.positions[i] += self.velocities[i] * dt
            self.resolve_collisions()

    def render(self, screen) -> None:
        for position in self.positions:
            pygame.draw.circle(
                screen, Colors.LightBlue, position, SimulationParams.particle_radius
            )

    def resolve_collisions(self) -> None:
        for i in range(SimulationParams.particle_count):
            # simulation bounding box
            half_bounds_size: Vector2 = (
                SimulationParams.get_bounds() / 2
                - Vector2.one * SimulationParams.particle_radius
            )

            if abs(self.positions[i].x) > half_bounds_size.x:
                self.positions[i].x = half_bounds_size.x * sign(self.positions[i].x)
                self.velocities[i].x *= -1 * SimulationParams.collision_dampening

            if abs(self.positions[i].y) > half_bounds_size.y:
                self.positions[i].y = half_bounds_size.y * sign(self.positions[i].y)
                self.velocities[i].y *= -1 * SimulationParams.collision_dampening

            # collisions between particles