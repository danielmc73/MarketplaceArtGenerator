from PIL import ImageDraw
from PIL import ImageFont

from .element import Element


class TextElement(Element):

    def __init__(
        self,
        text,
        x,
        y,
        size=40,
        color=(0, 0, 0),
    ):

        super().__init__(x, y)

        self.text = text

        self.size = size

        self.color = color

        self.font = ImageFont.load_default()

    def draw(self, image):

        draw = ImageDraw.Draw(image)

        draw.text(
            (
                self.x,
                self.y,
            ),
            self.text,
            fill=self.color,
            font=self.font,
        )
