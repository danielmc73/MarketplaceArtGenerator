"""Sports-stadium background element."""

from PIL import Image as PillowImage
from PIL import ImageDraw, ImageFilter
from PIL.Image import Image

from .base import Element


class StadiumBackground(Element):
    """Draw a dark, illuminated stadium backdrop with a grass field."""

    def __init__(self, width: int, height: int, *, z_index: int = -100) -> None:
        super().__init__(0, 0, z_index=z_index)
        self.width = width
        self.height = height

    def draw(self, image: Image) -> None:
        draw = ImageDraw.Draw(image)
        field_start = int(self.height * 0.68)
        for y in range(self.height):
            if y < field_start:
                ratio = y / field_start
                color = (5 + int(9 * ratio), 8 + int(13 * ratio), 12 + int(20 * ratio), 255)
            else:
                ratio = (y - field_start) / (self.height - field_start)
                color = (16 - int(8 * ratio), 72 - int(35 * ratio), 29 - int(14 * ratio), 255)
            draw.line((0, y, self.width, y), fill=color)

        lights = PillowImage.new("RGBA", image.size, (0, 0, 0, 0))
        light_draw = ImageDraw.Draw(lights)
        light_y = int(self.height * 0.13)
        for center_x in (80, 220, 980, 1120):
            for radius, alpha in ((105, 10), (65, 18), (30, 45)):
                light_draw.ellipse(
                    (center_x - radius, light_y - radius, center_x + radius, light_y + radius),
                    fill=(245, 250, 255, alpha),
                )
            light_draw.rectangle(
                (center_x - 38, light_y - 9, center_x + 38, light_y + 9),
                fill=(235, 240, 245, 120),
            )
        image.alpha_composite(lights.filter(ImageFilter.GaussianBlur(16)))
        image.alpha_composite(lights)

        horizon = int(self.height * 0.67)
        draw.line((0, horizon, self.width, horizon), fill=(235, 240, 220, 130), width=2)
        for x in range(-200, self.width + 200, 135):
            draw.line((x, self.height, self.width // 2, horizon), fill=(70, 127, 60, 100), width=3)
