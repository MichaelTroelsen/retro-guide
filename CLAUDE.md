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
|-------|-------------|
| Mac SE/30 | Copy buttons on code blocks |

That is the only outstanding gap. Verified 2026-07-18: `mac-se30-reference.html` contains no
`navigator.clipboard` call and no copy-button class; the four `copy` matches in it are prose and
68000 comments. Note its own changelog entry claims "Copy buttons on all 68030 assembly code
blocks" — that claim is false.

**Before adding to this table, grep for the feature.** The previous version of this table listed
eight further gaps (PET PCBWay/Tindie; BBC Micro and Amstrad CPC search, copy buttons and chip
modals; C64 chip modals) — **all eight were already implemented.** Chip modals are prefixed per
machine (`c64-chip-modal`, `cpc-chip-modal`, `pet-chip-modal`), so a generic `modal-overlay`
search returns zero and reads as absence. A zero result from one pattern is not evidence; check
the loose word first, then the underlying API, then inspect the matches. See issue #1.

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
