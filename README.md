# Marketplace Art Generator

Gerador de artes para marketplaces. A Entrega 1B fornece uma base grafica
testada: canvas RGBA de 1200 x 1200 px, elementos ordenados por camada e
exportacao para PNG, JPG ou WebP.

## Executar

No Windows, dentro da pasta do projeto:

```cmd
.venv\Scripts\activate
python -m pip install -e .
python main.py
python -m unittest discover -s tests -v
```

O comando principal cria sete artes:

- `output/01_principal_mercadolivre.png`: foto principal, sem textos.
- `output/02_kit_campeao.png`: capa premium esportiva do kit.
- `output/03_qualidade_especificacoes.png`: qualidade e especificacoes tecnicas.
- `output/04_duvidas_respondidas.png`: perguntas frequentes do kit.
- `output/05_bomba_manual_premium.png`: beneficios e medidas da bomba.
- `output/06_versatilidade.png`: aplicacoes compativeis da bomba.
- `output/07_presente_perfeito.png`: chamada final para presente.

## Fundos fotograficos

As artes usam fundos originais e realistas em `assets/backgrounds`:

- `stadium_night_v1.png`: capa esportiva;
- `quality_stage_v1.png`: qualidade e especificacoes;
- `versatility_field_v1.png`: aplicacoes compativeis;
- `gift_studio_v1.png`: chamada de presente.

Os textos continuam sendo renderizados pela aplicacao para garantir fidelidade
e facilidade de edicao.

As fotos fornecidas sao tratadas por perfil do produto: quando uma foto reunir
variantes de cor, a arte usa uma variante representativa sem ocultar a
informacao de envio sortido presente no layout.

## Estrutura da entrega

- `src/mag/core`: configuracoes do canvas.
- `src/mag/graphics`: canvas e renderizador.
- `src/mag/elements`: retangulos, texto e imagens.
- `src/mag/components`: badge, cards de beneficio e produto em destaque.
- `src/mag/layouts`: layouts especificos para cada imagem do anuncio.
- `tests`: validacao da renderizacao e exportacao.
