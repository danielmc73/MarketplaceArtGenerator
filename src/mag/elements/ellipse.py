"""Ellipse element."""

from PIL import ImageDraw
from PIL.Image import Image

from .base import Element


class Ellipse(Element):
    """Draw a filled ellipse, commonly used for a simple product shadow."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        fill: tuple[int, ...],
        *,
        visible: bool = True,
        z_index: int = 0,
    ) -> None:
        super().__init__(x, y, visible=visible, z_index=z_index)
        if width <= 0 or height <= 0:
            raise ValueError("Ellipse width and height must be positive.")
        self.width = width
        self.height = height
        self.fill = fill

    def draw(self, image: Image) -> None:
        ImageDraw.Draw(image).ellipse(
            (self.x, self.y, self.x + self.width, self.y + self.height),
            fill=self.fill,
        )
