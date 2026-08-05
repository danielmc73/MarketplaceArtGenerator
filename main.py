"""Generate the Mercado Livre image set for the ball-and-pump kit."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from mag import __version__
from mag.layouts import build_kit_campeao_image, build_principal_image, build_quality_image


def _product_images() -> tuple[Path, Path]:
    """Resolve the current product photos supplied in the asset folder."""
    product_dir = PROJECT_ROOT / "assets" / "products" / "kit_bola"
    images = sorted(path for path in product_dir.iterdir() if path.is_file())
    if len(images) < 2:
        raise FileNotFoundError("Adicione as fotos da bola e da bomba em assets/products/kit_bola.")
    pump = next((path for path in images if path.stem.startswith("723")), images[0])
    ball = next((path for path in images if path != pump), images[1])
    return ball, pump


def main() -> None:
    """Generate the first three marketplace images for the current kit."""
    ball, pump = _product_images()
    output_dir = PROJECT_ROOT / "output"
    artifacts = (
        ("Imagem principal", output_dir / "01_principal_mercadolivre.png", build_principal_image),
        ("Arte Kit Campeao", output_dir / "02_kit_campeao.png", build_kit_campeao_image),
        ("Arte de qualidade", output_dir / "03_qualidade_especificacoes.png", build_quality_image),
    )
    print(f"Marketplace Art Generator | versao {__version__}")
    for label, destination, builder in artifacts:
        builder(ball, pump).save(destination)
        print(f"{label} criada: {destination.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
