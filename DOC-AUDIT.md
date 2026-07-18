# Documentation Audit — retro-guide

**Audited:** 2026-07-18 · **Commit:** 868a03c · **Branch:** master
**Documents read:** 3 files, 6.5 KB (README.md, CLAUDE.md, PROJECT_INSTRUCTIONS.md) — all read in full
**Findings:** 2 P0 · 2 P1 · 1 P2 · 2 P3 — all HIGH confidence
**Filed as issues:** 7 findings grouped into 5 issues — [#1](../../issues/1) · [#2](../../issues/2) · [#3](../../issues/3) · [#4](../../issues/4) · [#5](../../issues/5)

| Finding | Issue |
|---|---|
| P0-1 stale gap tables | [#1](../../issues/1) |
| P0-2 wrong branch in sync URLs | [#2](../../issues/2) |
| P1-1 PROJECT_INSTRUCTIONS duplicate | [#3](../../issues/3) |
| P1-2 README watchdog install | [#4](../../issues/4) |
| P2-1 guide list in four places | [#3](../../issues/3) — resolved by deleting the file |
| P3-1 `rstrip(".git")` | [#5](../../issues/5) |
| P3-2 hardcoded `WATCH_DIR` | [#5](../../issues/5) |

---

## Ground truth

| Fact | Actual value | Source | Confidence |
|---|---|---|---|
| Branch | `master` | `git branch --show-current` | **HIGH** — direct |
| Remote | `github.com/MichaelTroelsen/retro-guide` | `git remote get-url origin` | **HIGH** — direct |
| Last commit | 868a03c, 2026-03-22 | `git log -1` | **HIGH** — direct |
| Manifest | none (no package.json/pyproject.toml) | `ls` | **HIGH** — direct |
| Guide files | 5 HTML, matching documented names | `ls *.html` | **HIGH** — direct |
| Version control | yes | `git rev-parse` | **HIGH** — direct |

---

## Findings

### P0-1 · Gap tables describe work that is already done

**Locations:** `CLAUDE.md:41-49`, `PROJECT_INSTRUCTIONS.md:42-50` (two copies of the same table)
**Claim:** PET needs PCBWay/Tindie; BBC Micro needs search, copy buttons, chip modals; Amstrad CPC needs the same three; C64 needs chip modals.
**Verified by:** per-guide pattern search, then inspection of each matched element to confirm it is a real implementation and not a stray string.

| Guide | Doc claims missing | Reality | Evidence | Confidence |
|---|---|---|---|---|
| PET | PCBWay/Tindie | **present** | 29 matches | **HIGH** |
| BBC Micro | search | **present** | `<input>` search element | **HIGH** |
| BBC Micro | copy buttons | **present** | 64 button matches + `navigator.clipboard` | **HIGH** |
| BBC Micro | chip modals | **present** | `chip-card`, `modal-overlay`, `modal-close`, `modal-body` | **HIGH** |
| Amstrad CPC | search | **present** | `<input id="cpcSearch" placeholder="SEARCH GUIDE… (press / to focus)">` | **HIGH** |
| Amstrad CPC | copy buttons | **present** | 19 matches + `navigator.clipboard` | **HIGH** |
| Amstrad CPC | chip modals | **present** | 22 matches | **HIGH** |
| C64 | chip modals | **present** | 16 matches | **HIGH** |
| Mac SE/30 | copy buttons | **genuinely missing** | zero `navigator.clipboard`, zero copy handlers | **HIGH** |

**8 of 9 claimed gaps are closed. Only Mac SE/30's copy buttons remain.**

**Consequence:** `CLAUDE.md` is agent-facing. An agent reading it will believe four guides lack features they already have, and may reimplement them — producing duplicate search bars and modal handlers in files that already work. This is the escalation case in `severity.md`: a stale gap-table in an agent-facing doc is P0, not P2.

**Fix:** Reduce both tables to the single open item (Mac SE/30 copy buttons), or delete the table from `PROJECT_INSTRUCTIONS.md` entirely per P1-1.

---

### P0-2 · Sync script generates dead URLs for every guide

**Location:** `retro_guide_sync.py:149`
**Claim (code, not doc):** `return f"{remote}/raw/main/{filename}"`
**Verified by:** `git branch --show-current` → `master`
**Actual:** the repo has no `main` branch. Every URL the watcher prints at startup 404s.
**Confidence:** **HIGH** — branch name read directly from git; the literal is unambiguous in the source.
**Consequence:** The documented workflow in `CLAUDE.md:63-68` is "fetch the latest file from the GitHub raw URL before editing". The URLs the script hands you for that purpose do not resolve. `README.md:40-44` has the correct `master` URLs, so the two sources disagree and the wrong one is the automated one.
**Fix:** `retro_guide_sync.py:149` → `/raw/master/`, or derive the branch with `git rev-parse --abbrev-ref HEAD`.

---

### P1-1 · `PROJECT_INSTRUCTIONS.md` is an unmaintained duplicate

**Location:** `PROJECT_INSTRUCTIONS.md` (whole file, 2.2 KB)
**Verified by:** section-by-section comparison against `CLAUDE.md`, plus filesystem checks on the referenced names.

Three independent defects, all absent from `CLAUDE.md`:

| Defect | Location | Evidence | Confidence |
|---|---|---|---|
| Unfilled placeholders | lines 9-21 | `YOUR_USER/YOUR_REPO` in all 5 URLs | **HIGH** |
| Wrong branch | lines 9-21 | `/main/` vs actual `master` | **HIGH** |
| Wrong filename | line 20 | `macintosh-se30-reference.html`; real file is `mac-se30-reference.html` | **HIGH** — `ls` confirms absence |

"Series standards" is duplicated verbatim from `CLAUDE.md:31-39`, and the gap table is a reformatted copy of `CLAUDE.md:41-49`.

**Consequence:** Every URL in this file is broken twice over. Nothing here is unique.
**Fix:** Delete the file, or reduce it to a pointer at `CLAUDE.md`.

---

### P1-2 · README contradicts the code on dependency installation

**Location:** `README.md:29-31` vs `CLAUDE.md:27`
**Claim (README):** `pip install watchdog` shown as a required step.
**Claim (CLAUDE.md):** "Requires `watchdog` (auto-installed on first run)."
**Verified by:** reading `retro_guide_sync.py:27-29` — an `except ImportError` branch runs `pip install watchdog` automatically.
**Actual:** **CLAUDE.md is correct; README is wrong.** The install is automatic.
**Confidence:** **HIGH** — the adjudicating code was read directly, not inferred from either document.
**Consequence:** Minor friction only. Recorded because it is the class of finding where a doc-vs-doc conflict is meaningless until the code decides — and here it does.
**Fix:** `README.md:29` → note that watchdog installs automatically on first run.

---

### P2-1 · Guide list maintained in four places

**Locations:** `README.md:7-13`, `CLAUDE.md:11-17`, `PROJECT_INSTRUCTIONS.md:8-21`, `retro_guide_sync.py:37` (`TRACKED_FILES`)
**Verified by:** comparing all four lists against `ls *.html`.
**Actual:** three copies agree with the filesystem; `PROJECT_INSTRUCTIONS.md` has already drifted (see P1-1).
**Confidence:** **HIGH** for the drift; the duplication itself is directly observable.
**Consequence:** This is the root cause of P1-1 rather than a separate defect. Four copies of one list means four places to forget.
**Canonical source should be:** `retro_guide_sync.py:TRACKED_FILES` — it is the only copy the software actually consumes, so it cannot silently drift without breaking the watcher.

---

### P3-1 · `remote.rstrip(".git")` strips characters, not a suffix

**Location:** `retro_guide_sync.py:148`
**Verified by:** reading the line; `str.rstrip` semantics are unambiguous.
**Actual:** `rstrip` removes any trailing characters in the set `{., g, i, t}`. A remote ending in e.g. `...retro-guit` or `...mygit` would lose characters.
**Confidence:** **HIGH** on the defect, **LOW** on it ever firing — the current remote (`retro-guide.git`) happens to strip correctly, and the URL is broken anyway by P0-2.
**Fix:** `remote[:-4] if remote.endswith(".git") else remote`, or `removesuffix(".git")` on Python 3.9+.

---

### P3-2 · Hardcoded machine-specific watch directory

**Location:** `retro_guide_sync.py:35` — `WATCH_DIR = r"C:\Users\mit\claude\retro-guide"`
**Verified by:** reading the assignment.
**Confidence:** **HIGH** on the fact; **judgment call** on whether it matters.
**Assessment:** `severity.md` escalates this to P1 when a repo is published and invites contributors. This repo is public on GitHub but has no LICENSE, no CONTRIBUTING, and reads as a personal tool — so it stays P3. `CLAUDE.md:27` already documents it as something to update.
**Fix (optional):** default to the script's own directory via `Path(__file__).parent`.

---

## Duplicated facts

| Fact | Locations | Currently agree? | Canonical source should be |
|---|---|---|---|
| Guide file list | README, CLAUDE.md, PROJECT_INSTRUCTIONS, `TRACKED_FILES` | **no** — PROJECT_INSTRUCTIONS drifted | `retro_guide_sync.py:TRACKED_FILES` |
| Series standards | CLAUDE.md:31-39, PROJECT_INSTRUCTIONS:32-40 | yes | `CLAUDE.md` |
| Gap table | CLAUDE.md:41-49, PROJECT_INSTRUCTIONS:44-50 | yes — both equally wrong | `CLAUDE.md`, corrected |
| Raw URLs | README:40-44, PROJECT_INSTRUCTIONS:9-21, `sync.py:149` | **no** — two of three wrong | derive from `git remote` at runtime |

---

## Verified clean

- All 5 documented guide filenames exist with exactly the documented names — `ls`
- No dead file references in README or CLAUDE.md — path extraction with `find` fallback (7 tokens checked, 0 missing)
- No exposed credentials — secrets scan across the repo
- README's raw URLs use the correct `master` branch — compared against `git branch`
- `start_sync.bat` and `retro_guide_sync.py` exist as documented
- Every guide has an interactive memory map and a changelog section, as the series standards require — pattern search, 5/5
- Auto-commit/debounce behaviour matches the documented 3 seconds — `DEBOUNCE_SECONDS` in source

---

## Unverifiable

| Claim | Location | Why unverifiable |
|---|---|---|
| "Authentic retro CRT theming per machine" | `CLAUDE.md:32` | Aesthetic judgment; CSS custom properties exist in all 5 files but authenticity cannot be checked mechanically |
| "no external dependencies except fonts/icons" | `CLAUDE.md:53` | Would require parsing every external URL in 2.7 MB of HTML; not attempted in this pass |

---

## Structural observations

**One root cause produced most findings.** P0-1, P1-1 and P2-1 are all the same thing: the guide list, the series standards and the gap table each exist in multiple copies, and the copy nobody opens (`PROJECT_INSTRUCTIONS.md`) rotted. Deleting that file resolves three findings at once.

**The docs describe an aspiration as a status.** The gap table was written when the gaps were real, then the work got done and the table stayed. Nothing about the workflow updates it — the watcher auto-commits guide edits within 3 seconds, so features ship without any prompt to revisit the documentation. Consider deriving the gap table from the guides themselves, or dropping it and letting the series standards stand alone as the specification.

**Two of the three highest findings are in code, not prose.** P0-2 and P3-1 are defects in `retro_guide_sync.py` that a documentation audit surfaced because the docs promised behaviour the code does not deliver. Fixing the docs to match the code would be the wrong direction here.

---

## Recommended order

1. **P0-1** — correct both gap tables to the single open item (Mac SE/30 copy buttons)
2. **P0-2** — `retro_guide_sync.py:149`: `main` → `master`, or derive the branch
3. **P1-1** — delete `PROJECT_INSTRUCTIONS.md` (also closes P2-1 and part of P0-1)
4. **P1-2** — README: note that watchdog auto-installs
5. **P3-1** — `removesuffix(".git")`

<!-- Regenerated on each audit. Git holds the history. -->
