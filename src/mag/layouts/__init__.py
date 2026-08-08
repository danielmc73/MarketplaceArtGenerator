"""Marketplace-specific composition layouts."""

from .mercadolivre_beneficios import build_benefits_image
from .mercadolivre_bomba import build_pump_image
from .mercadolivre_kit_campeao import build_kit_campeao_image
from .mercadolivre_principal import build_principal_image
from .mercadolivre_qualidade import build_quality_image
from .mercadolivre_duvidas import build_questions_image
from .mercadolivre_presente import build_gift_image
from .mercadolivre_versatilidade import build_versatility_image

__all__ = [
    "build_benefits_image",
    "build_pump_image",
    "build_kit_campeao_image",
    "build_principal_image",
    "build_quality_image",
    "build_questions_image",
    "build_gift_image",
    "build_versatility_image",
]
