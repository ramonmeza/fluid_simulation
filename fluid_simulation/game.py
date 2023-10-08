import pygame

from .colors import Colors

class Game:
    window: pygame.Surface
    screen: pygame.Surface

    def __init__(self, window_width: int, window_height: int, fullscreen: bool) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.screen = pygame.display.get_surface()
        
        if fullscreen != pygame.display.is_fullscreen():
            pygame.display.toggle_fullscreen()
        
    def update(self, dt: float) -> None:
        print(dt)
    
    def render(self) -> None:
        self.window.fill(Colors.Black)
        pygame.display.flip()

    def run(self) -> None:
        delta_clock: pygame.time.Clock = pygame.time.Clock()
        is_running: bool = True
        while is_running:
            dt: float = delta_clock.tick()
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    is_running = False
            self.update(dt)
            self.render()
