"""Application settings."""

from dataclasses import dataclass

from .constants import CANVAS_HEIGHT, CANVAS_WIDTH, DEFAULT_BACKGROUND, DEFAULT_DPI


@dataclass(slots=True)
class Settings:
    width: int = CANVAS_WIDTH
    height: int = CANVAS_HEIGHT
    background: tuple[int, int, int] = DEFAULT_BACKGROUND
    dpi: tuple[int, int] = DEFAULT_DPI
