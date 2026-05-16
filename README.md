# Green Cards PDF Splitter

[![CI](https://github.com/X-Limited/Green-Cards/actions/workflows/ci.yml/badge.svg)](https://github.com/X-Limited/Green-Cards/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

Python projekt pro automatické rozdělení PDF balíku zelených karet na samostatné PDF soubory.

## Funkce

- extrakce jednotlivých zelených karet z PDF
- automatické pojmenování podle SPZ/RZ
- mapování uživatelů z Excel souboru
- export jednotlivých PDF souborů
- GitHub-ready struktura projektu
- changelog a release notes

## Struktura projektu

```text
Green-Cards/
├── src/
├── data/
├── output/
├── tests/
├── README.md
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
└── RELEASE_NOTES.md
```

## Instalace

```bash
pip install -r requirements.txt
```

## Spuštění

```bash
python src/green_card_splitter.py
```

## License

[MIT](LICENSE) © 2026 X-Limited
