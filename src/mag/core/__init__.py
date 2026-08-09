"""Application configuration primitives."""

from .settings import Settings

__all__ = ["Settings"]
"""Core application settings and product configuration."""

from .product_config import CropBox, ProductAssets, load_product_assets

__all__ = ["CropBox", "ProductAssets", "load_product_assets"]
