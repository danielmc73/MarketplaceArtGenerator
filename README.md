# Marketplace Art Generator

Gerador de artes para marketplaces. A Entrega 1B fornece uma base gráfica testada: canvas RGBA de 1200 × 1200 px, elementos ordenados por camada e exportação para PNG, JPG ou WebP.

## Executar

No Windows, dentro da pasta do projeto:

```cmd
.venv\Scripts\activate
python -m pip install -e .
python main.py
python -m unittest discover -s tests -v
```

O comando principal cria `output/entrega_1c_componentes.png`.

## Estrutura da entrega

- `src/mag/core`: configurações do canvas.
- `src/mag/graphics`: canvas e renderizador.
- `src/mag/elements`: retângulos, texto e imagens.
- `src/mag/components`: badge, cards de beneficio e produto em destaque.
- `tests`: validação da renderização e exportação.
