"""Versatility layout for the included manual pump."""

from pathlib import Path

from mag.components import HeroProduct
from mag.elements import Ellipse, ImageElement, TextElement
from mag.graphics import Canvas
from mag.themes import SPORTS_PREMIUM


PROJECT_ROOT = Path(__file__).resolve().parents[3]
VERSATILITY_BACKGROUND = PROJECT_ROOT / "assets" / "backgrounds" / "versatility_field_v1.png"


def _activity(canvas: Canvas, code: str, label: str, x: int, y: int, color: tuple[int, int, int]) -> None:
    canvas.add(Ellipse(x, y, 175, 175, SPORTS_PREMIUM["white"], z_index=8))
    canvas.add(Ellipse(x + 10, y + 10, 155, 155, color, z_index=9))
    canvas.add(
        TextElement(
            code,
            x + 40,
            y + 61,
            size=43,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            label,
            x + 18,
            y + 190,
            size=23,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )


def build_versatility_image(
    _: str | Path,
    pump_path: str | Path,
    *,
    pump_crop: tuple[int, int, int, int] | None = None,
) -> Canvas:
    """Build the image presenting the pump's compatible applications."""
    canvas = Canvas()
    canvas.add(ImageElement(VERSATILITY_BACKGROUND, 0, 0, width=1200, height=1200, z_index=-100))
    canvas.add(
        TextElement(
            "PARA TODAS AS SUAS",
            66,
            44,
            size=50,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "AVENTURAS!",
            64,
            104,
            size=76,
            fill=SPORTS_PREMIUM["yellow"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "UM KIT, INFINITAS POSSIBILIDADES",
            66,
            201,
            size=25,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    HeroProduct(
        pump_path,
        970,
        50,
        height=205,
        crop=pump_crop,
        remove_light_background=True,
        shadow=True,
    ).add_to(canvas)
    _activity(canvas, "FUT", "FUTEBOL", 100, 335, (31, 117, 50))
    _activity(canvas, "VOL", "VOLEI", 510, 335, (39, 98, 180))
    _activity(canvas, "BAS", "BASQUETE", 920, 335, (189, 87, 38))
    _activity(canvas, "BOIA", "BOIAS", 100, 665, (220, 78, 139))
    _activity(canvas, "PISC", "PISCINAS", 510, 665, (35, 159, 218))
    _activity(canvas, "BAL", "BALOES", 920, 665, (166, 59, 185))
    canvas.add(
        TextElement(
            "IDEAL PARA CRIANCAS, JOVENS E ADULTOS",
            256,
            1080,
            size=27,
            fill=SPORTS_PREMIUM["yellow"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    return canvas
