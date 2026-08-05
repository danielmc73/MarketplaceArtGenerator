"""Hero product component."""

from pathlib import Path

from mag.elements import ImageElement
from mag.graphics import Canvas


class HeroProduct:
    """Place a prominent transparent product image in a composition."""

    def __init__(
        self,
        image_path: str | Path,
        x: int,
        y: int,
        *,
        width: int | None = None,
        height: int | None = None,
        crop: tuple[int, int, int, int] | None = None,
        clip_ellipse: bool = False,
        remove_light_background: bool = False,
        shadow: bool = True,
    ) -> None:
        self.image_path = Path(image_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.crop = crop
        self.clip_ellipse = clip_ellipse
        self.remove_light_background = remove_light_background
        self.shadow = shadow

    def add_to(self, canvas: Canvas) -> Canvas:
        """Add the product image to ``canvas``."""
        canvas.add(
            ImageElement(
                self.image_path,
                self.x,
                self.y,
                width=self.width,
                height=self.height,
                crop=self.crop,
                clip_ellipse=self.clip_ellipse,
                remove_light_background=self.remove_light_background,
                shadow=self.shadow,
                z_index=5,
            )
        )
        return canvas
