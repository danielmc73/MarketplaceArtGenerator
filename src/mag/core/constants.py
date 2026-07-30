"""Constantes globais do projeto."""

from pathlib import Path

# Diretórios
PROJECT_ROOT = Path(__file__).resolve().parents[3]

ASSETS_DIR = PROJECT_ROOT / "assets"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Canvas Mercado Livre
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1200

# Cor padrão
DEFAULT_BACKGROUND = (255, 255, 255)
WHITE = DEFAULT_BACKGROUND

# DPI para exportação
DEFAULT_DPI = (300, 300)
DPI = DEFAULT_DPI

# Formato padrão
DEFAULT_FORMAT = "PNG"
