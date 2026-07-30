"""Run the Entrega 1B demonstration."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from rich.console import Console
from rich.panel import Panel

from mag import __version__
from mag.elements import Rectangle, TextElement
from mag.graphics import Canvas

console = Console()


def main() -> None:
    """Create the first graphical engine demo."""
    console.print()
    console.print(
        Panel.fit(
            "[bold cyan]Marketplace Art Generator[/]\n"
            f"Entrega 1B · versão {__version__}\n"
            "Canvas e elementos gráficos prontos.",
            title="MAG",
        )
    )

    canvas = Canvas()
    canvas.add(Rectangle(60, 60, 1080, 190, (255, 225, 0), radius=28))
    canvas.add(
        TextElement(
            "Marketplace Art Generator", 110, 118, size=48, fill=(32, 32, 32)
        )
    )
    canvas.add(
        TextElement(
            "Base visual para artes de marketplace", 110, 182, size=26, fill=(32, 32, 32)
        )
    )
    destination = canvas.save(PROJECT_ROOT / "output" / "entrega_1b_demo.png")
    console.print("[green]Canvas renderizado com sucesso.[/]")
    console.print(f"[cyan]Arquivo:[/] {destination.relative_to(PROJECT_ROOT)}")
    console.print()


if __name__ == "__main__":
    main()
