"""Frequently asked questions layout for the kit."""

from pathlib import Path

from mag.components import HeroProduct
from mag.elements import Ellipse, Rectangle, TextElement
from mag.graphics import Canvas
from mag.products import PRIMARY_PUMP_CROP
from mag.themes import SPORTS_PREMIUM


def _faq(canvas: Canvas, question: str, answer: str, y: int) -> None:
    canvas.add(Ellipse(68, y + 2, 42, 42, SPORTS_PREMIUM["red"], z_index=10))
    canvas.add(
        TextElement(
            "?",
            82,
            y + 8,
            size=24,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(
        TextElement(
            question,
            132,
            y,
            size=23,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(
        TextElement(
            answer,
            132,
            y + 31,
            size=17,
            fill=(58, 58, 58),
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )


def build_questions_image(ball_path: str | Path, pump_path: str | Path) -> Canvas:
    """Build the customer-objection answer image for the product listing."""
    canvas = Canvas()
    canvas.add(Rectangle(0, 0, 1200, 1200, (248, 248, 246), z_index=-10))
    canvas.add(
        TextElement(
            "CHEGA DE D\u00daVIDAS!",
            64,
            42,
            size=58,
            fill=SPORTS_PREMIUM["ink"],
            font_path=SPORTS_PREMIUM["title_font"],
            z_index=10,
        )
    )
    canvas.add(Rectangle(0, 135, 770, 112, SPORTS_PREMIUM["red"], z_index=9))
    canvas.add(
        TextElement(
            "AS D\u00daVIDAS MAIS COMUNS,",
            62,
            153,
            size=31,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    canvas.add(
        TextElement(
            "RESPONDIDAS:",
            62,
            194,
            size=31,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=10,
        )
    )
    _faq(canvas, "A BOLA E BOA QUALIDADE?", "Sim! Material resistente para partidas e treinos.", 320)
    _faq(canvas, "PERDE AR MUITO RAPIDO?", "Use a pressao indicada: de 4 a 6 PSI.", 435)
    _faq(canvas, "A BOMBA FUNCIONA BEM?", "Sim! Acompanha bico agulha para encher a bola.", 550)
    _faq(canvas, "SERVE EM OUTRAS BOLAS?", "Compativel com bolas e pequenos inflaveis.", 665)
    _faq(canvas, "COMO E O ENVIO?", "Consulte o prazo informado no anuncio.", 780)
    HeroProduct(
        ball_path,
        760,
        290,
        width=400,
        crop=(0, 0, 600, 630),
        clip_ellipse=True,
        shadow=True,
    ).add_to(canvas)
    HeroProduct(
        pump_path,
        900,
        670,
        height=290,
        crop=PRIMARY_PUMP_CROP,
        remove_light_background=True,
        shadow=True,
    ).add_to(canvas)
    canvas.add(Rectangle(48, 1024, 1104, 110, SPORTS_PREMIUM["ink"], radius=22, z_index=10))
    canvas.add(
        TextElement(
            "COMPRA 100% SEGURA",
            125,
            1055,
            size=28,
            fill=SPORTS_PREMIUM["white"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    canvas.add(Rectangle(590, 1041, 2, 76, (105, 105, 105), z_index=11))
    canvas.add(
        TextElement(
            "SATISFACAO GARANTIDA",
            650,
            1055,
            size=24,
            fill=SPORTS_PREMIUM["yellow"],
            font_path=SPORTS_PREMIUM["body_font"],
            z_index=11,
        )
    )
    return canvas
