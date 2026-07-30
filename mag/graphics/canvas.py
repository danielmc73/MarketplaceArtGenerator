"""Canvas principal do projeto."""

from pathlib import Path

from PIL import Image

from mag.core.settings import Settings
from .element import Element


class Canvas:

    def __init__(self, settings: Settings | None = None):

        self.settings = settings or Settings()

        self.image = Image.new(
            "RGB",
            (
                self.settings.width,
                self.settings.height,
            ),
            self.settings.background,
        )

        self.elements: list[Element] = []

    @property
    def width(self):

        return self.image.width

    @property
    def height(self):

        return self.image.height

    def add(self, element):

        self.elements.append(element)

    def render(self):

        for element in self.elements:

            if element.visible:

                element.draw(self.image)

    def save(self, path: str | Path):

        self.render()

        Path(path).parent.mkdir(parents=True, exist_ok=True)

        self.image.save(
            path,
            dpi=self.settings.dpi,
        )

    def show(self):

        self.image.show()
