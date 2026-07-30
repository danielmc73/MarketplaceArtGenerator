from pathlib import Path

from PIL import Image

from .element import Element


class ImageElement(Element):

    def __init__(
        self,
        path: str | Path,
        x: int,
        y: int,
        width: int | None = None,
        height: int | None = None,
    ):

        super().__init__(x, y)

        self.image = Image.open(path).convert("RGBA")

        if width and height:

            self.image = self.image.resize(
                (
                    width,
                    height,
                )
            )

    def draw(self, canvas):

        canvas.paste(
            self.image,
            (
                self.x,
                self.y,
            ),
            self.image,
        )
