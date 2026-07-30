"""Canvas used to assemble a marketplace image."""

from pathlib import Path

from PIL import Image

from mag.core.settings import Settings
from mag.elements import Element

from .renderer import render_elements


class Canvas:
    """A layered RGBA canvas with deterministic rendering and export."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()
        self._elements: list[Element] = []
        self._image = Image.new("RGBA", (self.settings.width, self.settings.height), (*self.settings.background, 255))

    @property
    def width(self) -> int:
        return self._image.width

    @property
    def height(self) -> int:
        return self._image.height

    def add(self, element: Element) -> "Canvas":
        self._elements.append(element)
        return self

    def render(self) -> Image.Image:
        self._image = Image.new("RGBA", (self.settings.width, self.settings.height), (*self.settings.background, 255))
        render_elements(self._image, self._elements)
        return self._image

    def save(self, path: str | Path) -> Path:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        image = self.render()
        if destination.suffix.lower() in {".jpg", ".jpeg"}:
            image = image.convert("RGB")
        image.save(destination, dpi=self.settings.dpi)
        return destination
