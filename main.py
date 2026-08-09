"""Generate the Mercado Livre image set for the ball-and-pump kit."""

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from mag import __version__
from mag.core import load_product_assets
from mag.layouts import (
    build_gift_image,
    build_kit_campeao_image,
    build_principal_image,
    build_pump_image,
    build_quality_image,
    build_questions_image,
    build_versatility_image,
)


def _arguments() -> argparse.Namespace:
    """Parse the optional product and output locations."""
    parser = argparse.ArgumentParser(description="Generate marketplace product images.")
    parser.add_argument(
        "--product-dir",
        type=Path,
        default=PROJECT_ROOT / "assets" / "products" / "kit_bola",
        help="Folder containing config.json and product images.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "output",
        help="Destination folder for generated images.",
    )
    return parser.parse_args()


def main() -> None:
    """Generate all seven marketplace images for the current kit."""
    arguments = _arguments()
    product = load_product_assets(arguments.product_dir)
    ball, pump = product.ball, product.pump
    output_dir = arguments.output_dir.resolve()
    artifacts = (
        ("Imagem principal", output_dir / "01_principal_mercadolivre.png", build_principal_image),
        ("Arte Kit Campeao", output_dir / "02_kit_campeao.png", build_kit_campeao_image),
        ("Arte de qualidade", output_dir / "03_qualidade_especificacoes.png", build_quality_image),
        ("Arte de duvidas", output_dir / "04_duvidas_respondidas.png", build_questions_image),
        ("Arte da bomba", output_dir / "05_bomba_manual_premium.png", build_pump_image),
        ("Arte de versatilidade", output_dir / "06_versatilidade.png", build_versatility_image),
        ("Arte presente perfeito", output_dir / "07_presente_perfeito.png", build_gift_image),
    )
    print(f"Marketplace Art Generator | versao {__version__}")
    print(f"Produto: {product.name}")
    for label, destination, builder in artifacts:
        builder(ball, pump, pump_crop=product.pump_crop).save(destination)
        print(f"{label} criada: {destination.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
