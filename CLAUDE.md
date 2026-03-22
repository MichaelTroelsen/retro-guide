# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A collection of 5 single-file HTML reference guides for classic computer systems, auto-synced to GitHub via a Python file-watcher script.

## The 5 guides

| File | System |
|------|--------|
| `C64_Development_Reference.html` | Commodore 64 |
| `bbc-micro-reference.html` | BBC Micro |
| `commodore-pet-reference.html` | Commodore PET |
| `amstrad_cpc_reference.html` | Amstrad CPC |
| `mac-se30-reference.html` | Macintosh SE/30 |

## Running the sync watcher

```bash
python retro_guide_sync.py
# or on Windows:
start_sync.bat
```

Requires `watchdog` (auto-installed on first run). The watcher monitors `WATCH_DIR` at the top of `retro_guide_sync.py` — update this path if your guides live elsewhere. It debounces 3 seconds after each save, then runs `git add`, `git commit`, and `git push` automatically.

## Series standards (apply to all guides)

Every guide must have:
- Authentic retro CRT theming per machine
- Tabbed navigation with sticky header
- Search bar with `/` keyboard shortcut to focus
- Copy buttons on all code blocks
- Clickable chip cards with detail modals
- Interactive memory map
- PCBWay Community + Tindie links in Hardware/Makers section
- Version history changelog section

## Current implementation gaps

| Guide | Needs |
|-------|-------|
| PET | PCBWay/Tindie section |
| BBC Micro | Search, copy buttons, chip modals |
| Amstrad CPC | Search, copy buttons, chip modals |
| C64 | Chip modals |
| Mac SE/30 | Copy buttons |

## Guide architecture (all guides follow this pattern)

Each guide is a **self-contained single HTML file** with all CSS and JS embedded — no external dependencies except fonts/icons. Key layout structure:

- Fixed/sticky header with machine-specific color theme and search input
- Tabbed navigation (inline JS, no framework)
- Sidebar TOC (C64 uses 300px fixed sidebar; others use tab-based layout)
- CSS custom properties (`--primary`, `--accent`, etc.) for theming
- Chip/component cards that open detail modals on click
- Memory map rendered inline with HTML/CSS grids
- Code blocks with copy-to-clipboard buttons (plain JS `navigator.clipboard`)

## Working with guides in Claude.ai (web)

The intended workflow when editing guides in a Claude.ai chat session:
1. Fetch the latest file from GitHub raw URL before editing
2. Edit and return the full updated file
3. Save locally — the watcher auto-commits and pushes

GitHub repo: `https://github.com/MichaelTroelsen/retro-guide`
