from abc import ABC, abstractmethod

from PIL.Image import Image


class Element(ABC):
    """
    Classe base de todos os elementos gráficos.
    """

    def __init__(
        self,
        x: int,
        y: int,
    ):

        self.x = x
        self.y = y

        self.visible = True

    @abstractmethod
    def draw(self, image: Image):
        ...
