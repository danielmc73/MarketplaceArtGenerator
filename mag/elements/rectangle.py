from PIL import ImageDraw

from .element import Element


class Rectangle(Element):

    def __init__(
        self,
        x,
        y,
        width,
        height,
        color,
    ):

        super().__init__(x, y)

        self.width = width

        self.height = height

        self.color = color

    def draw(self, image):

        draw = ImageDraw.Draw(image)

        draw.rectangle(
            (
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
            ),
            fill=self.color,
        )
