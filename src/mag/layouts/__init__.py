"""Marketplace-specific composition layouts."""

from .mercadolivre_beneficios import build_benefits_image
from .mercadolivre_kit_campeao import build_kit_campeao_image
from .mercadolivre_principal import build_principal_image

__all__ = [
    "build_benefits_image",
    "build_kit_campeao_image",
    "build_principal_image",
]
