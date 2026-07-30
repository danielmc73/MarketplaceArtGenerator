"""Image element."""

from pathlib import Path

from PIL import Image
from PIL.Image import Image as PillowImage

from .base import Element


class ImageElement(Element):
    """Place an image on the canvas while preserving transparency."""

    def __init__(self, path: str | Path, x: int, y: int, *, width: int | None = None, height: int | None = None, visible: bool = True, z_index: int = 0) -> None:
        super().__init__(x, y, visible=visible, z_index=z_index)
        self.path = Path(path)
        if not self.path.is_file():
            raise FileNotFoundError(f"Image not found: {self.path}")
        self.width, self.height = width, height

    def draw(self, image: PillowImage) -> None:
        with Image.open(self.path) as source:
            product = source.convert("RGBA")
        if self.width is not None or self.height is not None:
            width = self.width or round(product.width * self.height / product.height)
            height = self.height or round(product.height * self.width / product.width)
            product = product.resize((width, height), Image.Resampling.LANCZOS)
        image.alpha_composite(product, dest=(self.x, self.y))
