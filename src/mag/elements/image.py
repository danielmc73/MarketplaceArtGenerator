"""Image element."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter
from PIL.Image import Image as PillowImage

from .base import Element


class ImageElement(Element):
    """Place an image on the canvas while preserving transparency."""

    def __init__(self, path: str | Path, x: int, y: int, *, width: int | None = None, height: int | None = None, crop: tuple[int, int, int, int] | None = None, clip_ellipse: bool = False, remove_light_background: bool = False, shadow: bool = False, visible: bool = True, z_index: int = 0) -> None:
        super().__init__(x, y, visible=visible, z_index=z_index)
        self.path = Path(path)
        if not self.path.is_file():
            raise FileNotFoundError(f"Image not found: {self.path}")
        self.width, self.height = width, height
        self.crop = crop
        self.clip_ellipse = clip_ellipse
        self.remove_light_background = remove_light_background
        self.shadow = shadow

    def _remove_light_background(self, product: PillowImage) -> PillowImage:
        """Make edge-connected near-white pixels transparent without affecting inner whites."""
        pixels = product.load()
        width, height = product.size
        seen: set[tuple[int, int]] = set()
        pending = [(x, y) for x in range(width) for y in (0, height - 1)]
        pending += [(x, y) for y in range(height) for x in (0, width - 1)]
        while pending:
            x, y = pending.pop()
            if (x, y) in seen or not (0 <= x < width and 0 <= y < height):
                continue
            red, green, blue, alpha = pixels[x, y]
            if alpha == 0 or min(red, green, blue) < 238:
                continue
            seen.add((x, y))
            pixels[x, y] = (red, green, blue, 0)
            pending.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))
        return product

    def _clip_ellipse(self, product: PillowImage) -> PillowImage:
        mask = Image.new("L", product.size, 0)
        margin_x = max(2, round(product.width * 0.015))
        margin_y = max(2, round(product.height * 0.015))
        ImageDraw.Draw(mask).ellipse(
            (margin_x, margin_y, product.width - margin_x, product.height - margin_y),
            fill=255,
        )
        product.putalpha(Image.composite(product.getchannel("A"), Image.new("L", product.size, 0), mask))
        return product

    def draw(self, image: PillowImage) -> None:
        with Image.open(self.path) as source:
            product = source.convert("RGBA")
        if self.crop:
            product = product.crop(self.crop)
        if self.width is not None or self.height is not None:
            width = self.width or round(product.width * self.height / product.height)
            height = self.height or round(product.height * self.width / product.width)
            product = product.resize((width, height), Image.Resampling.LANCZOS)
        if self.remove_light_background:
            product = self._remove_light_background(product)
        if self.clip_ellipse:
            product = self._clip_ellipse(product)
        if self.shadow:
            alpha = product.getchannel("A").filter(ImageFilter.GaussianBlur(12))
            shadow = Image.new("RGBA", product.size, (0, 0, 0, 95))
            shadow.putalpha(alpha.point(lambda value: value // 3))
            image.alpha_composite(shadow, dest=(self.x + 14, self.y + 20))
        image.alpha_composite(product, dest=(self.x, self.y))
