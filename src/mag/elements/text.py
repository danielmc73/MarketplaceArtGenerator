"""Text element."""

from pathlib import Path

from PIL import ImageDraw, ImageFont
from PIL.Image import Image

from .base import Element


class TextElement(Element):
    """Draw one line of text with an optional TrueType font."""

    def __init__(self, text: str, x: int, y: int, *, size: int = 40, fill: tuple[int, ...] = (0, 0, 0), font_path: str | Path | None = None, visible: bool = True, z_index: int = 0) -> None:
        super().__init__(x, y, visible=visible, z_index=z_index)
        if size <= 0:
            raise ValueError("Text size must be positive.")
        self.text, self.size, self.fill = text, size, fill
        self.font_path = Path(font_path) if font_path else None

    def _font(self) -> ImageFont.ImageFont:
        if self.font_path:
            return ImageFont.truetype(str(self.font_path), self.size)
        return ImageFont.load_default(size=self.size)

    def draw(self, image: Image) -> None:
        ImageDraw.Draw(image).text((self.x, self.y), self.text, fill=self.fill, font=self._font())
