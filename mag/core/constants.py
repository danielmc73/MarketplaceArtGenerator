"""Constantes globais do projeto."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ASSETS_DIR = PROJECT_ROOT / "assets"
OUTPUT_DIR = PROJECT_ROOT / "output"

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1200

DEFAULT_BACKGROUND = (255, 255, 255)
WHITE = DEFAULT_BACKGROUND

DEFAULT_DPI = (300, 300)
DPI = DEFAULT_DPI

DEFAULT_FORMAT = "PNG"
