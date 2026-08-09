"""Loading and validation for product image manifests."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

CropBox = tuple[int, int, int, int]


@dataclass(frozen=True, slots=True)
class ProductAssets:
    """Resolved images and metadata required to render one product set."""

    name: str
    marketplace: str
    ball: Path
    pump: Path
    pump_crop: CropBox | None = None


def _crop_box(value: object, manifest_path: Path) -> CropBox | None:
    """Validate an optional source-image crop rectangle."""
    if value is None:
        return None
    if not isinstance(value, list) or len(value) != 4 or not all(
        isinstance(coordinate, int) for coordinate in value
    ):
        raise ValueError(f"Invalid pump.primary_crop in product manifest: {manifest_path}")
    left, top, right, bottom = value
    if left < 0 or top < 0 or right <= left or bottom <= top:
        raise ValueError(f"Invalid pump.primary_crop bounds in product manifest: {manifest_path}")
    return left, top, right, bottom


def load_product_assets(product_dir: str | Path) -> ProductAssets:
    """Load a product manifest and resolve its required image files.

    Each product folder must contain a ``config.json`` with ``images.ball`` and
    ``images.pump`` relative to that folder.  Explicit configuration prevents
    an unrelated image from being selected by filename ordering.
    """
    directory = Path(product_dir)
    manifest_path = directory / "config.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Product manifest not found: {manifest_path}")

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        images = manifest["images"]
        ball = directory / images["ball"]
        pump = directory / images["pump"]
        pump_crop = _crop_box(manifest.get("pump", {}).get("primary_crop"), manifest_path)
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise ValueError(f"Invalid product manifest: {manifest_path}") from error

    missing = [path.name for path in (ball, pump) if not path.is_file()]
    if missing:
        names = ", ".join(missing)
        raise FileNotFoundError(f"Configured product image(s) not found: {names}")

    return ProductAssets(
        name=str(manifest.get("name", directory.name)),
        marketplace=str(manifest.get("marketplace", "mercadolivre")),
        ball=ball,
        pump=pump,
        pump_crop=pump_crop,
    )
