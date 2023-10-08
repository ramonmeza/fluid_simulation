import abc

class IUpdatable(abc.ABC):
    def update(dt: float) -> None:
        raise NotImplementedError
