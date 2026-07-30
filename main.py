"""Generate the first Mercado Livre image for the ball-and-pump kit."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from mag import __version__
from mag.layouts import build_principal_image


def _product_images() -> tuple[Path, Path]:
    """Resolve the current product photos supplied in the asset folder."""
    product_dir = PROJECT_ROOT / "assets" / "products" / "kit_bola"
    images = sorted(path for path in product_dir.iterdir() if path.is_file())
    if len(images) < 2:
        raise FileNotFoundError(
            "Adicione as fotos da bola e da bomba em assets/products/kit_bola."
        )
    pump = next((path for path in images if path.stem.startswith("723")), images[0])
    ball = next((path for path in images if path != pump), images[1])
    return ball, pump


def main() -> None:
    """Generate the text-free primary image for the current kit."""
    ball, pump = _product_images()
    destination = PROJECT_ROOT / "output" / "01_principal_mercadolivre.png"
    build_principal_image(ball, pump).save(destination)
    print("Marketplace Art Generator")
    print(f"Entrega 1D | versao {__version__}")
    print(f"Imagem principal criada: {destination.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
