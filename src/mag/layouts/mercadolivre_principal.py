"""Text-free main image layout for a Mercado Livre listing."""

from pathlib import Path

from mag.elements import Ellipse
from mag.graphics import Canvas
from mag.components import HeroProduct
from mag.products import PRIMARY_PUMP_CROP


def build_principal_image(ball_path: str | Path, pump_path: str | Path) -> Canvas:
    """Build a 1200 px square primary image for the ball-and-pump kit.

    The layout intentionally contains no text, badges, borders, or promotional
    graphics so it is suitable as the main image in a Mercado Livre listing.
    """
    canvas = Canvas()
    canvas.add(Ellipse(122, 937, 640, 55, (226, 226, 226), z_index=1))
    canvas.add(Ellipse(785, 940, 260, 42, (230, 230, 230), z_index=1))
    HeroProduct(ball_path, 90, 185, width=700, remove_light_background=True).add_to(canvas)
    HeroProduct(
        pump_path,
        840,
        260,
        height=620,
        crop=PRIMARY_PUMP_CROP,
        remove_light_background=True,
    ).add_to(canvas)
    return canvas
