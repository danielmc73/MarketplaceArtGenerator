"""Marketplace-specific composition layouts."""

from .mercadolivre_beneficios import build_benefits_image
from .mercadolivre_principal import build_principal_image

__all__ = ["build_benefits_image", "build_principal_image"]
