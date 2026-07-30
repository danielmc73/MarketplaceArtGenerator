from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from mag import __version__
from mag.graphics import Canvas

console = Console()


def main() -> None:
    console.print()

    console.print(
        Panel.fit(
            f"Marketplace Art Generator\n\nVersão {__version__}",
            title="MAG",
        )
    )

    output = Path("output")
    output.mkdir(exist_ok=True)

    canvas = Canvas()
    canvas.save(output / "canvas.png")

    console.print()
    console.print("[green]Canvas criado com sucesso![/]")
    console.print("[cyan]Arquivo:[/] output/canvas.png")
    console.print()


if __name__ == "__main__":
    main()
