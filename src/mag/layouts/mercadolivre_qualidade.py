"""Quality and technical specifications layout for the kit."""

from pathlib import Path

from mag.components import HeroProduct
from mag.elements import Ellipse, Rectangle, StadiumBackground, TextElement
from mag.graphics import Canvas
from mag.themes import SPORTS_PREMIUM


def _bullet(canvas: Canvas, number: str, title: str, detail: str, y: int) -> None:
    canvas.add(Ellipse(70, y, 58, 58, SPORTS_PREMIUM["yellow"], z_index=10))
    canvas.add(Ellipse(76, y + 6, 46, 46, SPORTS_PREMIUM["ink"], z_index=11))
    canvas.add(TextElement(number, 90, y + 14, size=25, fill=SPORTS_PREMIUM["yellow"], font_path=SPORTS_PREMIUM["body_font"], z_index=12))
    canvas.add(TextElement(title, 150, y + 3, size=25, fill=SPORTS_PREMIUM["yellow"], font_path=SPORTS_PREMIUM["body_font"], z_index=12))
    canvas.add(TextElement(detail, 150, y + 34, size=18, fill=SPORTS_PREMIUM["white"], font_path=SPORTS_PREMIUM["body_font"], z_index=12))


def _metric(canvas: Canvas, value: str, label: str, x: int) -> None:
    canvas.add(Ellipse(x, 1032, 56, 56, SPORTS_PREMIUM["yellow"], z_index=10))
    canvas.add(TextElement(value, x + 72, 1038, size=24, fill=SPORTS_PREMIUM["yellow"], font_path=SPORTS_PREMIUM["body_font"], z_index=11))
    canvas.add(TextElement(label, x + 72, 1072, size=16, fill=SPORTS_PREMIUM["white"], font_path=SPORTS_PREMIUM["body_font"], z_index=11))


def build_quality_image(ball_path: str | Path, pump_path: str | Path) -> Canvas:
    """Build a premium technical-detail image for the ball-and-pump kit."""
    canvas = Canvas()
    canvas.add(StadiumBackground(1200, 1200))
    canvas.add(TextElement("QUALIDADE QUE VOC\u00ca SENTE,", 62, 50, size=48, fill=SPORTS_PREMIUM["white"], font_path=SPORTS_PREMIUM["title_font"], z_index=10))
    canvas.add(TextElement("DESEMPENHO QUE VOC\u00ca V\u00ca!", 62, 107, size=46, fill=SPORTS_PREMIUM["yellow"], font_path=SPORTS_PREMIUM["title_font"], z_index=10))
    _bullet(canvas, "5", "TAMANHO OFICIAL", "Padrao ideal para seus jogos.", 230)
    _bullet(canvas, "P", "MATERIAL PREMIUM", "Resistente para o uso diario.", 350)
    _bullet(canvas, "G", "OTIMA PEGADA", "Mais controle nos passes e chutes.", 470)
    _bullet(canvas, "A", "CAMARA DE AR", "Mantem a pressao por mais tempo.", 590)
    _bullet(canvas, "C", "IDEAL PARA CAMPO", "Gramado natural ou sintetico.", 710)
    HeroProduct(ball_path, 592, 212, width=550, crop=(0, 0, 600, 630), clip_ellipse=True, shadow=True).add_to(canvas)
    HeroProduct(pump_path, 705, 735, width=310, remove_light_background=True, shadow=True).add_to(canvas)
    canvas.add(Rectangle(0, 970, 1200, 230, (7, 8, 10, 240), z_index=8))
    _metric(canvas, "410-450g", "PESO OFICIAL", 60)
    _metric(canvas, "68-70cm", "CIRCUNFERENCIA", 390)
    _metric(canvas, "4 A 6 PSI", "PRESSAO RECOMENDADA", 735)
    return canvas
