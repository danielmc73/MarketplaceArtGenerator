"""Dedicated pump feature image for the kit."""

from pathlib import Path

from mag.components import HeroProduct
from mag.elements import Ellipse, Rectangle, TextElement
from mag.graphics import Canvas
from mag.products import PRIMARY_PUMP_CROP
from mag.themes import SPORTS_PREMIUM

BLUE = (21, 68, 160)


def _benefit(canvas: Canvas, title: str, detail: str, y: int) -> None:
    canvas.add(Ellipse(598, y, 38, 38, BLUE, z_index=10))
    canvas.add(
        TextElement(
            "+",
            608,
            y + 3,
            size=23,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(
        TextElement(
            title,
            655,
            y - 2,
            size=24,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(
        TextElement(
            detail,
            655,
            y + 27,
            size=17,
            fill=(64, 64, 64),
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )


def build_pump_image(_: str | Path, pump_path: str | Path) -> Canvas:
    """Build a feature-driven image focused on the manual pump."""
    canvas = Canvas()
    canvas.add(Rectangle(0, 0, 1200, 1200, (247, 247, 245), z_index=-10))
    canvas.add(
        TextElement(
            "BOMBA DE AR",
            60,
            48,
            size=56,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "MANUAL PREMIUM",
            60,
            112,
            size=48,
            fill=BLUE,
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "PEQUENA NO TAMANHO, GIGANTE NA PRATICIDADE!",
            62,
            185,
            size=22,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    canvas.add(Rectangle(542, 245, 610, 550, (255, 255, 255), radius=22, z_index=4))
    _benefit(canvas, "INFLACAO RAPIDA", "Mais praticidade para encher.", 285)
    _benefit(canvas, "BICO DE METAL", "Conexao firme e segura.", 390)
    _benefit(canvas, "MULTIUSO", "Bolas e pequenos inflaveis.", 495)
    _benefit(canvas, "LEVE E PORTATIL", "Leve para onde quiser.", 600)
    _benefit(canvas, "CORES SORTIDAS", "Envio conforme disponibilidade.", 705)
    HeroProduct(
        pump_path,
        160,
        250,
        height=770,
        crop=PRIMARY_PUMP_CROP,
        remove_light_background=True,
        shadow=True,
    ).add_to(canvas)
    canvas.add(Rectangle(62, 865, 430, 150, (255, 255, 255), radius=18, z_index=6))
    canvas.add(
        TextElement(
            "MEDIDAS:",
            92,
            890,
            size=25,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=7,
        )
    )
    canvas.add(TextElement("BOMBA: 28 cm x 3,5 cm", 92, 928, size=19, fill=SPORTS_PREMIUM["ink"], font_path=SPORTS_PREMIUM["body_font"], z_index=7))
    canvas.add(TextElement("BICO: 3,5 cm", 92, 960, size=19, fill=SPORTS_PREMIUM["ink"], font_path=SPORTS_PREMIUM["body_font"], z_index=7))
    canvas.add(Rectangle(48, 1065, 1104, 82, BLUE, radius=18, z_index=10))
    canvas.add(
        TextElement(
            "1 BOMBA + 1 BICO AGULHA INCLUSO",
            285,
            1088,
            size=27,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    return canvas
