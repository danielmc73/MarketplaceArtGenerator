from dataclasses import dataclass

from PIL.Image import Image


@dataclass(slots=True)
class Layer:
    """
    Representa uma camada da composição.
    """

    name: str

    image: Image

    visible: bool = True

    opacity: float = 1.0
