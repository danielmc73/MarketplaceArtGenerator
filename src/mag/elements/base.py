"""Base types for drawable elements."""

from abc import ABC, abstractmethod

from PIL.Image import Image


class Element(ABC):
    """An object that can render itself onto a Pillow image."""

    def __init__(self, x: int, y: int, *, visible: bool = True, z_index: int = 0) -> None:
        self.x = x
        self.y = y
        self.visible = visible
        self.z_index = z_index

    @abstractmethod
    def draw(self, image: Image) -> None:
        """Draw the element onto ``image``."""
