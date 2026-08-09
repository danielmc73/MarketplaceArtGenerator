"""Application configuration primitives."""

from .settings import Settings

__all__ = ["Settings"]
"""Core application settings and product configuration."""

from .product_config import ProductAssets, load_product_assets

__all__ = ["ProductAssets", "load_product_assets"]
