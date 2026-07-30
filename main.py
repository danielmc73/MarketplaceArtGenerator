"""Run the Entrega 1C component demonstration."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from mag import __version__
from mag.components import Badge, BenefitCard
from mag.elements import Rectangle, TextElement
from mag.graphics import Canvas

def main() -> None:
    """Create a product-benefit composition using reusable components."""
    print("Marketplace Art Generator")
    print(f"Entrega 1C | versao {__version__}")
    print("Componentes reutilizaveis prontos.\n")

    canvas = Canvas()
    canvas.add(Rectangle(0, 0, 1200, 300, (255, 225, 0)))
    canvas.add(TextElement("KIT BOLA + BOMBA", 76, 95, size=58, fill=(32, 32, 32)))
    canvas.add(
        TextElement("Tudo para comecar a jogar", 76, 182, size=30, fill=(32, 32, 32))
    )
    Badge("PRONTO PARA JOGAR", 820, 95).add_to(canvas)
    BenefitCard(
        "Tamanho oficial n. 5",
        "Ideal para partidas e treinos.",
        76,
        410,
    ).add_to(canvas)
    BenefitCard(
        "Bomba inclusa",
        "Encha a bola de forma pratica.",
        624,
        410,
    ).add_to(canvas)
    BenefitCard(
        "Kit versatil",
        "Bomba compativel com diversos inflaveis.",
        76,
        600,
    ).add_to(canvas)
    BenefitCard(
        "Compra segura",
        "Produto com garantia do vendedor.",
        624,
        600,
    ).add_to(canvas)

    destination = canvas.save(PROJECT_ROOT / "output" / "entrega_1c_componentes.png")
    print("Composicao de componentes criada com sucesso.")
    print(f"Arquivo: {destination.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
