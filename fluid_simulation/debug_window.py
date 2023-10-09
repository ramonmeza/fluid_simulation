import dearpygui.dearpygui as dpg
import pygame

from .colors import Colors
from .game_object import GameObject
from .simulation_params import SimulationParams
from .vector2 import Vector2


class DebugWindow(GameObject):
    GRAVITY_SLIDER_ID: str = "GravitySlider"
    PARTICLE_RADIUS_SLIDER_ID: str = "ParticleRadiusSlider"
    BOUNDS_SIZE_SLIDER_ID: str = "BoundsSizeSlider"
    COLLISION_DAMPENING_SLIDER_ID: str = "CollisionDampeningSlider"

    def __init__(self) -> None:
        super().__init__()
        dpg.create_context()
        dpg.create_viewport(title="Debug Window", width=600, height=200)
        dpg.setup_dearpygui()
        self._construct_window()
        dpg.show_viewport()

    def _construct_window(self):
        window = dpg.add_window(label="Debug Window")
        self.gravity_slider = dpg.add_slider_float(
            tag=DebugWindow.GRAVITY_SLIDER_ID,
            parent=window,
            label="Gravity",
            min_value=-1000.0,
            max_value=1000.0,
            default_value=SimulationParams.gravity,
            callback=self.update_gravity,
        )
        self.particle_radius_slider = dpg.add_slider_float(
            tag=DebugWindow.PARTICLE_RADIUS_SLIDER_ID,
            parent=window,
            label="ParticleRadius",
            min_value=-100.0,
            max_value=100.0,
            default_value=SimulationParams.particle_radius,
            callback=self.update_particle_radius,
        )
        self.bounds_size_sliders = dpg.add_slider_floatx(
            tag=DebugWindow.BOUNDS_SIZE_SLIDER_ID,
            parent=window,
            label="Bounds Size",
            size=2,
            min_value=0,
            max_value=1920,
            default_value=[
                SimulationParams.bounds_size.x,
                SimulationParams.bounds_size.y,
            ],
            callback=self.update_bounds_size,
        )
        self.collision_dampening_slider = dpg.add_slider_float(
            tag=DebugWindow.COLLISION_DAMPENING_SLIDER_ID,
            parent=window,
            label="Collision Dampening",
            min_value=0.0,
            max_value=2.0,
            default_value=SimulationParams.collision_dampening,
            callback=self.update_collision_dampening,
        )
        dpg.set_primary_window(window, True)

    def update_gravity(sender):
        val = dpg.get_value(DebugWindow.GRAVITY_SLIDER_ID)
        SimulationParams.gravity = val

    def update_particle_radius(sender):
        val = dpg.get_value(DebugWindow.PARTICLE_RADIUS_SLIDER_ID)
        SimulationParams.particle_radius = val

    def update_bounds_size(sender):
        val = dpg.get_value(DebugWindow.BOUNDS_SIZE_SLIDER_ID)
        x = val[0]
        y = val[1]
        SimulationParams.bounds_size = Vector2(x, y)

    def update_collision_dampening(sender):
        val = dpg.get_value(DebugWindow.COLLISION_DAMPENING_SLIDER_ID)
        SimulationParams.collision_dampening = val

    def update(self, dt: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        dpg.render_dearpygui_frame()
        pos = Vector2(
            (screen.get_width() / 2) - (SimulationParams.bounds_size.x / 2),
            (screen.get_height() / 2) - (SimulationParams.bounds_size.y / 2),
        )
        pygame.draw.rect(
            screen,
            Colors.Green,
            pygame.Rect(
                pos.x,
                pos.y,
                SimulationParams.bounds_size.x,
                SimulationParams.bounds_size.y,
            ),
            1,
        )

    def destroy(self) -> None:
        dpg.destroy_context()
