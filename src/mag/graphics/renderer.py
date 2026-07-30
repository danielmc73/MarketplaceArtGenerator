"""Rendering helpers."""

from collections.abc import Iterable

from mag.elements import Element


def render_elements(image, elements: Iterable[Element]) -> None:
    """Render visible elements in ascending z-index order."""
    for element in sorted(elements, key=lambda item: item.z_index):
        if element.visible:
            element.draw(image)
