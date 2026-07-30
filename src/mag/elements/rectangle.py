"""Rectangle element."""

from PIL import ImageDraw
from PIL.Image import Image

from .base import Element


class Rectangle(Element):
    """Draw a filled rectangle, optionally with rounded corners."""

    def __init__(self, x: int, y: int, width: int, height: int, fill: tuple[int, ...], *, radius: int = 0, visible: bool = True, z_index: int = 0) -> None:
        super().__init__(x, y, visible=visible, z_index=z_index)
        if width <= 0 or height <= 0:
            raise ValueError("Rectangle width and height must be positive.")
        self.width, self.height, self.fill, self.radius = width, height, fill, max(0, radius)

    def draw(self, image: Image) -> None:
        draw = ImageDraw.Draw(image)
        bounds = (self.x, self.y, self.x + self.width, self.y + self.height)
        if self.radius:
            draw.rounded_rectangle(bounds, radius=self.radius, fill=self.fill)
        else:
            draw.rectangle(bounds, fill=self.fill)
