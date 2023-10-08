import abc

import pygame


class GameObject(abc.ABC):
    def update(self, dt: float) -> None:
        raise NotImplementedError("update() not implemented")

    def render(self, screen: pygame.Surface) -> None:
        raise NotImplementedError("render() not implemented")

    def destroy(self) -> None:
        pass
