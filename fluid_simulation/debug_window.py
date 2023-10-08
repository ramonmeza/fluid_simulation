import dearpygui.dearpygui as dpg
import pygame

from .game_object import GameObject
from .simulation_params import SimulationParams


class DebugWindow(GameObject):
    GRAVITY_SLIDER_ID: str = "GravitySlider"
    PARTICLE_RADIUS_SLIDER_ID: str = "ParticleRadiusSlider"

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
            min_value=-100.0,
            max_value=100.0,
            default_value=SimulationParams.gravity,
            callback=self.update_gravity,
        )
        self.particle_radius = dpg.add_slider_float(
            tag=DebugWindow.PARTICLE_RADIUS_SLIDER_ID,
            parent=window,
            label="ParticleRadius",
            min_value=-100.0,
            max_value=100.0,
            default_value=SimulationParams.particle_radius,
            callback=self.update_particle_radius,
        )
        dpg.set_primary_window(window, True)

    def update_gravity(sender):
        val = dpg.get_value(DebugWindow.GRAVITY_SLIDER_ID)
        print(f"Gravity changed: {val}")
        SimulationParams.gravity = val

    def update_particle_radius(sender):
        val = dpg.get_value(DebugWindow.PARTICLE_RADIUS_SLIDER_ID)
        print(f"Particle Radius changed: {val}")
        SimulationParams.particle_radius = val

    def update(self, dt: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        dpg.render_dearpygui_frame()

    def destroy(self) -> None:
        dpg.destroy_context()
