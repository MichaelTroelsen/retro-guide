# Retro Computing Guide Series — Project Instructions

## My 5 guide files live on GitHub. Fetch them at session start.

### Raw URLs (always latest version):

```
commodore-pet-reference.html:
  https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/commodore-pet-reference.html

bbc-micro-reference.html:
  https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/bbc-micro-reference.html

amstrad_cpc_reference.html:
  https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/amstrad_cpc_reference.html

C64_Development_Reference.html:
  https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/C64_Development_Reference.html

macintosh-se30-reference.html:
  https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/macintosh-se30-reference.html
```

## How I work across guides

- Each guide is an independent single-file HTML document
- When I edit a guide, I return the full updated file for download
- The watcher script (retro_guide_sync.py) auto-pushes saves to GitHub
- Fetch the file before editing to ensure I have the latest version

## Series standards (apply to all 5 guides)

- Authentic retro CRT theming per machine
- Tabbed navigation with sticky header
- Search bar with keyboard navigation (/ to focus)
- Copy buttons on all code blocks
- Clickable chip cards with detail modals
- Interactive memory map
- PCBWay Community + Tindie in Hardware/Makers section
- Version history changelog section

## Quick reference: which guide needs what

| Guide        | Missing PCBWay/Tindie | Missing search | Missing copy buttons | Missing chip modals |
|:-------------|:---------------------:|:--------------:|:--------------------:|:-------------------:|
| PET          | ✗ needs adding        | —              | —                    | —                   |
| BBC Micro    | —                     | ✗              | ✗                    | ✗                   |
| Amstrad CPC  | —                     | ✗              | ✗                    | ✗                   |
| C64          | —                     | —              | —                    | ✗                   |
| Mac SE/30    | —                     | —              | ✗                    | —                   |
