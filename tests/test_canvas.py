"""Regression tests for the first graphics engine release."""

from pathlib import Path
import sys
import tempfile
import unittest

SOURCE_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SOURCE_DIR))

from PIL import Image

from mag.elements import Rectangle
from mag.graphics import Canvas
from mag.components import Badge, BenefitCard


class CanvasTests(unittest.TestCase):
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
