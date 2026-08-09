"""Regression tests for the first graphics engine release."""

from pathlib import Path
import sys
import tempfile
import unittest

SOURCE_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SOURCE_DIR))

from PIL import Image

from mag.core import load_product_assets
from mag.elements import Rectangle
from mag.graphics import Canvas
from mag.components import Badge, BenefitCard
from mag.layouts import build_benefits_image, build_gift_image, build_kit_campeao_image, build_principal_image, build_pump_image, build_quality_image, build_questions_image, build_versatility_image


def _kit_assets() -> tuple[Path, Path]:
    """Return the configured source images for the test product."""
    product_dir = Path(__file__).resolve().parents[1] / "assets" / "products" / "kit_bola"
    product = load_product_assets(product_dir)
    return product.ball, product.pump


class CanvasTests(unittest.TestCase):
    def test_product_manifest_resolves_required_images(self) -> None:
        product_dir = Path(__file__).resolve().parents[1] / "assets" / "products" / "kit_bola"
        product = load_product_assets(product_dir)
        self.assertEqual(product.name, "Kit Bola de Futebol + Bomba de Ar")
        self.assertTrue(product.ball.is_file())
        self.assertTrue(product.pump.is_file())

    def test_canvas_exports_1200_square_png(self) -> None:
        canvas = Canvas().add(Rectangle(0, 0, 20, 20, (255, 225, 0)))
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "example.png"
            canvas.save(output)
            self.assertTrue(output.is_file())
            with Image.open(output) as rendered:
                self.assertEqual(rendered.size, (1200, 1200))
                self.assertEqual(rendered.getpixel((5, 5))[:3], (255, 225, 0))

    def test_components_render_on_canvas(self) -> None:
        canvas = Canvas()
        Badge("TEST", 20, 20).add_to(canvas)
        BenefitCard("Title", "Description", 20, 120).add_to(canvas)
        rendered = canvas.render()
        self.assertEqual(rendered.getpixel((30, 30))[:3], (32, 32, 32))
        self.assertEqual(rendered.getpixel((25, 160))[:3], (255, 225, 0))

    def test_principal_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_principal_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_benefits_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_benefits_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_kit_campeao_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_kit_campeao_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_quality_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_quality_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_questions_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_questions_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_pump_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_pump_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_versatility_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_versatility_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))

    def test_gift_layout_is_square(self) -> None:
        ball, pump = _kit_assets()
        canvas = build_gift_image(ball, pump)
        self.assertEqual(canvas.render().size, (1200, 1200))
