"""Benefit card component."""

from mag.elements import Rectangle, TextElement
from mag.graphics import Canvas


class BenefitCard:
    """A reusable informational card with a clear title and supporting text."""

    def __init__(
        self,
        title: str,
        description: str,
        x: int,
        y: int,
        *,
        width: int = 500,
        height: int = 145,
        accent: tuple[int, int, int] = (255, 225, 0),
    ) -> None:
        self.title = title
        self.description = description
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.accent = accent

    def add_to(self, canvas: Canvas) -> Canvas:
        """Add the card to ``canvas``."""
        canvas.add(
            Rectangle(
                self.x,
                self.y,
                self.width,
                self.height,
                (245, 245, 245),
                radius=22,
                z_index=1,
            )
        )
        canvas.add(
            Rectangle(
                self.x,
                self.y,
                12,
                self.height,
                self.accent,
                radius=6,
                z_index=2,
            )
        )
        canvas.add(
            TextElement(
                self.title,
                self.x + 38,
                self.y + 28,
                size=28,
                fill=(32, 32, 32),
                z_index=3,
            )
        )
        canvas.add(
            TextElement(
                self.description,
                self.x + 38,
                self.y + 76,
                size=20,
                fill=(83, 83, 83),
                z_index=3,
            )
        )
        return canvas
