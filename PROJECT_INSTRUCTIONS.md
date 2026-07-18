# Retro Computing Guide Series — Project Instructions

Paste this into a Claude.ai web project. For Claude Code, `CLAUDE.md` is the file that
matters — it is the source of truth for series standards and outstanding work, and this
file deliberately does not repeat them.

## My 5 guide files live on GitHub. Fetch them at session start.

### Raw URLs (always latest version)

```
commodore-pet-reference.html:
  https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/commodore-pet-reference.html

bbc-micro-reference.html:
  https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/bbc-micro-reference.html

amstrad_cpc_reference.html:
  https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/amstrad_cpc_reference.html

C64_Development_Reference.html:
  https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/C64_Development_Reference.html

mac-se30-reference.html:
  https://raw.githubusercontent.com/MichaelTroelsen/retro-guide/master/mac-se30-reference.html
```

The branch is **`master`**, not `main`. Getting this wrong 404s every link.

## How I work across guides

- Each guide is an independent single-file HTML document
- When I edit a guide, I return the full updated file for download
- The watcher script (`retro_guide_sync.py`) auto-pushes saves to GitHub
- Fetch the file before editing to ensure I have the latest version

## Series standards and outstanding work

**See `CLAUDE.md`.** Both live there, in one copy.

Until 2026-07-18 this file carried its own copy of the series standards and a matrix of
per-guide gaps. The matrix listed nine missing features, of which **eight already existed** —
it had drifted because nothing read this file. Duplicating that content here is what caused
the drift, so it is not duplicated any more. See issues #1 and #3.
