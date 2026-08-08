"""Premium sports cover for the ball-and-pump kit."""

from pathlib import Path

from mag.components import HeroProduct
from mag.elements import Ellipse, ImageElement, Rectangle, TextElement
from mag.graphics import Canvas
from mag.themes import SPORTS_PREMIUM

PROJECT_ROOT = Path(__file__).resolve().parents[3]
STADIUM_BACKGROUND = PROJECT_ROOT / "assets" / "backgrounds" / "stadium_night_v1.png"


def _feature(canvas: Canvas, label: str, x: int) -> None:
    canvas.add(Rectangle(x, 1050, 236, 100, (8, 8, 10, 215), radius=12, z_index=8))
    canvas.add(Ellipse(x + 105, 1061, 24, 24, SPORTS_PREMIUM["yellow"], z_index=9))
    canvas.add(
        TextElement(
            label,
            x + 24,
            1098,
            size=17,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=9,
        )
    )


def build_kit_campeao_image(ball_path: str | Path, pump_path: str | Path) -> Canvas:
    """Build the high-impact campaign cover inspired by the approved reference."""
    canvas = Canvas()
    canvas.add(ImageElement(STADIUM_BACKGROUND, 0, 0, width=1200, height=1200, z_index=-100))
    canvas.add(
        TextElement(
            "KIT",
            64,
            35,
            size=88,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["title_font"],
            stroke_width=2,
            stroke_fill=SPORTS_PREMIUM["ink"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "CAMPE\u00c3O",
            62,
            120,
            size=122,
            fill=SPORTS_PREMIUM["yellow"],
            font_path=SPORTS_PREMIUM["title_font"],
            stroke_width=3,
            stroke_fill=SPORTS_PREMIUM["ink"],
            z_index=10,
        )
    )
    canvas.add(Rectangle(70, 275, 555, 76, SPORTS_PREMIUM["red"], radius=10, z_index=10))
    canvas.add(
        TextElement(
            "BOLA + BOMBA DE AR",
            93,
            291,
            size=37,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(
        TextElement(
            "TUDO O QUE VOC\u00ca PRECISA",
            74,
            376,
            size=30,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "PARA O JOGO!",
            74,
            419,
            size=36,
            fill=SPORTS_PREMIUM["yellow"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    HeroProduct(
        pump_path,
        83,
        470,
        width=270,
        remove_light_background=True,
        shadow=True,
    ).add_to(canvas)
    HeroProduct(
        ball_path,
        390,
        395,
        width=610,
        crop=(0, 0, 600, 630),
        clip_ellipse=True,
        shadow=True,
    ).add_to(canvas)
    _feature(canvas, "QUALIDADE", 60)
    _feature(canvas, "DESEMPENHO", 330)
    _feature(canvas, "DURABILIDADE", 600)
    _feature(canvas, "PRONTO PARA JOGAR", 870)
    return canvas
