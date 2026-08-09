"""Benefit-focused secondary image for a Mercado Livre listing."""

from pathlib import Path

from mag.components import BenefitCard, HeroProduct
from mag.elements import Rectangle, TextElement
from mag.graphics import Canvas


def build_benefits_image(
    ball_path: str | Path,
    pump_path: str | Path,
    *,
    pump_crop: tuple[int, int, int, int] | None = None,
) -> Canvas:
    """Build the second kit image with concise, customer-facing benefits."""
    canvas = Canvas()
    canvas.add(Rectangle(0, 0, 1200, 270, (255, 225, 0)))
    canvas.add(TextElement("KIT BOLA + BOMBA", 76, 62, size=54, fill=(32, 32, 32)))
    canvas.add(
        TextElement(
            "Tudo o que voce precisa para jogar", 76, 150, size=30, fill=(32, 32, 32)
        )
    )
    HeroProduct(ball_path, 50, 310, width=510).add_to(canvas)
    HeroProduct(
        pump_path,
        565,
        365,
        height=380,
        crop=pump_crop,
        remove_light_background=True,
    ).add_to(canvas)
    BenefitCard(
        "Bola tamanho n. 5",
        "Tamanho oficial para seus jogos.",
        750,
        335,
        width=375,
        height=130,
    ).add_to(canvas)
    BenefitCard(
        "Bomba inclusa",
        "Praticidade para encher quando precisar.",
        750,
        495,
        width=375,
        height=130,
    ).add_to(canvas)
    BenefitCard(
        "Mais tempo jogando",
        "Leve o kit para treinos e diversao.",
        750,
        655,
        width=375,
        height=130,
    ).add_to(canvas)
    canvas.add(Rectangle(76, 940, 1048, 118, (32, 32, 32), radius=28))
    canvas.add(
        TextElement(
            "PRONTO PARA A PROXIMA PARTIDA", 314, 978, size=32, fill=(255, 255, 255)
        )
    )
    return canvas
