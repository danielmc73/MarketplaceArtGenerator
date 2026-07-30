"""Badge component."""

from mag.elements import Rectangle, TextElement
from mag.graphics import Canvas


class Badge:
    """A compact, rounded label used to emphasize a product attribute."""

    def __init__(
        self,
        text: str,
        x: int,
        y: int,
        *,
        width: int = 270,
        height: int = 54,
        fill: tuple[int, int, int] = (32, 32, 32),
        text_fill: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.text_fill = text_fill

    def add_to(self, canvas: Canvas) -> Canvas:
        """Add the badge primitives to ``canvas``."""
        canvas.add(
            Rectangle(
                self.x,
                self.y,
                self.width,
                self.height,
                self.fill,
                radius=self.height // 2,
                z_index=10,
            )
        )
        canvas.add(
            TextElement(
                self.text,
                self.x + 22,
                self.y + 14,
                size=22,
                fill=self.text_fill,
                z_index=11,
            )
        )
        return canvas
