"""Canvas principal do projeto."""

from pathlib import Path

from PIL import Image

from .settings import Settings


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

    @property
    def width(self):
        return self.image.width

    @property
    def height(self):
        return self.image.height

    def save(self, path: str | Path):
        self.image.save(
            path,
            dpi=self.settings.dpi,
        )

    def show(self):
        self.image.show()
