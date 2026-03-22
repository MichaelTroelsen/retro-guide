# Retro Computing Guide Series

A collection of comprehensive, single-file HTML reference guides for classic computer systems. Each guide is a self-contained interactive document with authentic retro CRT theming, requiring no build step or external dependencies.

## Guides

| Guide | System |
|-------|--------|
| `C64_Development_Reference.html` | Commodore 64 |
| `bbc-micro-reference.html` | BBC Micro |
| `commodore-pet-reference.html` | Commodore PET |
| `amstrad_cpc_reference.html` | Amstrad CPC |
| `mac-se30-reference.html` | Macintosh SE/30 |

Each guide includes:
- Tabbed navigation with sticky header and machine-specific CRT colour theme
- Search bar (`/` to focus)
- Copy buttons on all code blocks
- Clickable chip/component cards with detail modals
- Interactive memory map
- Hardware/Makers section (PCBWay Community + Tindie)
- Version history changelog

## Auto-sync

`retro_guide_sync.py` watches the repo folder and automatically commits and pushes any guide changes to GitHub within 3 seconds of saving.

```bash
pip install watchdog
python retro_guide_sync.py
```

Or on Windows, double-click `start_sync.bat`.

## Raw file URLs

Use these to fetch the latest version of a guide directly:

```
https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/C64_Development_Reference.html
https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/bbc-micro-reference.html
https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/commodore-pet-reference.html
https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/amstrad_cpc_reference.html
https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/mac-se30-reference.html
```
