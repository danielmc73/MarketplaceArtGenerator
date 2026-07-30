from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from mag.graphics import Canvas

console = Console()


def main():

    console.print()

    console.print(
        Panel.fit(
            "[bold cyan]MarketplaceArtGenerator[/]\n"
            "Entrega 1B\n"
            "Canvas Engine",
            title="MAG",
        )
    )

    canvas = Canvas()

    output = Path("output")

    output.mkdir(exist_ok=True)

    canvas.save(output / "canvas_1200.png")

    console.print()

    console.print("[green]✓ Canvas criado[/]")

    console.print("[cyan]output/canvas_1200.png[/]")

    console.print()


if __name__ == "__main__":

    main()
