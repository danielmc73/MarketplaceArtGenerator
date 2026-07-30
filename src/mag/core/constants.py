"""Global project constants."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ASSETS_DIR = PROJECT_ROOT / "assets"
OUTPUT_DIR = PROJECT_ROOT / "output"
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1200
DEFAULT_BACKGROUND = (255, 255, 255)
DEFAULT_DPI = (300, 300)
