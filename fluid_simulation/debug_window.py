import dearpygui.dearpygui as dpg
import pygame

from .game_object import GameObject


class DebugWindow(GameObject):
    def __init__(self) -> None:
        super().__init__()
        dpg.create_context()
        dpg.create_viewport(title="Custom Title", width=600, height=200)
        dpg.setup_dearpygui()
        with dpg.window(tag="Debug Window", label="Debug Window"):
            dpg.add_text("Hello, world")

        dpg.show_viewport()
        dpg.set_primary_window("Debug Window", True)
            
    def update(self, dt: float) -> None:
        pass
    
    def render(self, screen: pygame.Surface) -> None:
        dpg.render_dearpygui_frame()
    
    def destroy(self) -> None:
        dpg.destroy_context()