from pathlib import Path
import sys

from rich.console import Console
from rich.panel import Panel

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from version import __version__

console = Console()


def main() -> None:
    console.print()

    console.print(
        Panel.fit(
            f"[bold cyan]Marketplace Art Generator[/]\n\n"
            f"Versão: [green]{__version__}[/green]\n"
            "Status: Projeto iniciado com sucesso.",
            title="MAG",
            border_style="blue",
        )
    )

    console.print()


if __name__ == "__main__":
    main()
