"""Gift-oriented final call-to-action layout."""

from pathlib import Path

from mag.components import HeroProduct
from mag.elements import Ellipse, ImageElement, Rectangle, TextElement
from mag.graphics import Canvas
from mag.themes import SPORTS_PREMIUM


PROJECT_ROOT = Path(__file__).resolve().parents[3]
GIFT_BACKGROUND = PROJECT_ROOT / "assets" / "backgrounds" / "gift_studio_v1.png"


def _gift_box(canvas: Canvas) -> None:
    """Draw a decorative gift box without introducing a fake product."""
    canvas.add(Rectangle(800, 480, 288, 318, (18, 18, 20), radius=12, z_index=8))
    canvas.add(Rectangle(776, 448, 336, 68, (25, 25, 28), radius=10, z_index=9))
    canvas.add(Rectangle(930, 448, 46, 350, SPORTS_PREMIUM["yellow"], z_index=10))
    canvas.add(Rectangle(776, 470, 336, 35, SPORTS_PREMIUM["yellow"], z_index=10))
    canvas.add(Ellipse(861, 398, 110, 82, SPORTS_PREMIUM["yellow"], z_index=11))
    canvas.add(Ellipse(937, 398, 110, 82, SPORTS_PREMIUM["yellow"], z_index=11))
    canvas.add(Ellipse(930, 418, 62, 62, (245, 185, 0), z_index=12))
    canvas.add(
        TextElement(
            "KIT",
            862,
            575,
            size=42,
            fill=SPORTS_PREMIUM["yellow"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=12,
        )
    )


def _benefit(canvas: Canvas, code: str, label: str, x: int) -> None:
    canvas.add(Ellipse(x + 74, 918, 72, 72, (250, 250, 248), z_index=10))
    canvas.add(
        TextElement(
            code,
            x + 93,
            936,
            size=30,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(
        TextElement(
            label,
            x + 14,
            1013,
            size=18,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )


def build_gift_image(
    ball_path: str | Path,
    pump_path: str | Path,
    *,
    pump_crop: tuple[int, int, int, int] | None = None,
) -> Canvas:
    """Build the seventh image, positioning the kit as a useful gift option."""
    canvas = Canvas()
    canvas.add(ImageElement(GIFT_BACKGROUND, 0, 0, width=1200, height=1200, z_index=-100))
    for x, y in ((55, 58), (315, 36), (1080, 72), (1140, 215), (72, 795), (1115, 785)):
        canvas.add(Rectangle(x, y, 16, 28, SPORTS_PREMIUM["yellow"], radius=3, z_index=4))
    canvas.add(
        TextElement(
            "PRESENTE PERFEITO",
            105,
            52,
            size=61,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(Rectangle(270, 132, 662, 72, SPORTS_PREMIUM["red"], radius=10, z_index=9))
    canvas.add(
        TextElement(
            "PARA QUEM AMA ESPORTE!",
            334,
            148,
            size=33,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    HeroProduct(ball_path, 75, 330, width=510, crop=(0, 0, 600, 630), clip_ellipse=True, shadow=True).add_to(canvas)
    HeroProduct(
        pump_path,
        600,
        455,
        height=300,
        crop=pump_crop,
        remove_light_background=True,
        shadow=True,
    ).add_to(canvas)
    _gift_box(canvas)
    canvas.add(
        TextElement(
            "UMA OPCAO COMPLETA PARA",
            118,
            790,
            size=28,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "CRIANCAS E ADOLESCENTES",
            118,
            830,
            size=34,
            fill=SPORTS_PREMIUM["red"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    _benefit(canvas, "+", "OTIMA OPCAO", 85)
    _benefit(canvas, "+", "RESISTENTE", 355)
    _benefit(canvas, "+", "QUALIDADE", 625)
    _benefit(canvas, "+", "SATISFACAO", 895)
    canvas.add(Rectangle(68, 1095, 1064, 76, SPORTS_PREMIUM["red"], radius=18, z_index=10))
    canvas.add(
        TextElement(
            "GARANTA JA O SEU KIT CAMPEAO!",
            305,
            1115,
            size=29,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    return canvas
