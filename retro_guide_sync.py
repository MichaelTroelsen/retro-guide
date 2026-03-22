#!/usr/bin/env python3
"""
retro_guide_sync.py
Auto-syncs your 5 retro computing HTML/MD guides to GitHub.
Whenever you save a file, it commits and pushes within 3 seconds.

Setup:
  pip install watchdog
  python retro_guide_sync.py

Requirements:
  - Git installed and in PATH
  - GitHub repo already created and cloned locally
  - WATCH_DIR set to your local folder containing the 5 guide files
"""

import subprocess
import time
import sys
import os
from pathlib import Path
from datetime import datetime

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("Installing watchdog...")
    subprocess.run([sys.executable, "-m", "pip", "install", "watchdog"], check=True)
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

# ── CONFIGURE THESE ─────────────────────────────────────────────────────────

WATCH_DIR = r"C:\Users\mit\Downloads\retro-guides"   # folder with your 5 guide files

TRACKED_FILES = [
    "commodore-pet-reference.html",
    "bbc-micro-reference.html",
    "amstrad_cpc_reference.html",
    "commodore-64-reference.html",       # adjust if different name
    "macintosh-se30-reference.html",     # adjust if different name
]

DEBOUNCE_SECONDS = 3   # wait this long after last save before committing

# ── END CONFIG ───────────────────────────────────────────────────────────────

GUIDE_NAMES = {
    "commodore-pet-reference.html":    "Commodore PET",
    "bbc-micro-reference.html":        "BBC Micro",
    "amstrad_cpc_reference.html":      "Amstrad CPC",
    "commodore-64-reference.html":     "Commodore 64",
    "macintosh-se30-reference.html":   "Macintosh SE/30",
    "C64_Development_SID_Music_Resources.md": "Commodore 64 (MD)",
    "C64_Development_Reference.html":  "Commodore 64 HTML",
}


class GuideHandler(FileSystemEventHandler):
    def __init__(self):
        self.pending = {}   # filename -> timestamp of last change

    def on_modified(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.name in TRACKED_FILES:
            self.pending[path.name] = time.time()
            print(f"  [{timestamp()}] Change detected: {path.name}")

    def on_created(self, event):
        self.on_modified(event)

    def flush_pending(self):
        """Call regularly. Commits any files whose debounce period has elapsed."""
        now = time.time()
        ready = [f for f, t in self.pending.items() if now - t >= DEBOUNCE_SECONDS]
        if not ready:
            return
        for f in ready:
            del self.pending[f]
        commit_files(ready)


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Git error: {result.stderr.strip()}")
        return False
    return True


def commit_files(filenames):
    """Stage, commit, and push the given filenames."""
    cwd = WATCH_DIR

    # Stage only the changed guide files
    for f in filenames:
        run(["git", "add", f], cwd=cwd)

    # Build commit message
    guides = [GUIDE_NAMES.get(f, f) for f in filenames]
    if len(guides) == 1:
        msg = f"Update {guides[0]}"
    else:
        msg = f"Update {', '.join(guides[:-1])} and {guides[-1]}"
    msg += f" [{timestamp()}]"

    # Check if there's actually anything staged
    status = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=cwd, capture_output=True, text=True
    )
    if not status.stdout.strip():
        print(f"  [{timestamp()}] No changes to commit (file unchanged on disk).")
        return

    ok = run(["git", "commit", "-m", msg], cwd=cwd)
    if not ok:
        return

    ok = run(["git", "push"], cwd=cwd)
    if ok:
        print(f"\n  ✓ [{timestamp()}] Pushed: {msg}")
        for f in filenames:
            print(f"    → {raw_url(f)}")
        print()
    else:
        print(f"  [{timestamp()}] Push failed — check your GitHub credentials.")


def raw_url(filename):
    """Try to derive the raw GitHub URL from git remote."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=WATCH_DIR, capture_output=True, text=True
        )
        remote = result.stdout.strip()
        # Convert SSH or HTTPS remote to raw URL
        # SSH: git@github.com:user/repo.git
        # HTTPS: https://github.com/user/repo.git
        if remote.startswith("git@github.com:"):
            remote = remote.replace("git@github.com:", "https://github.com/")
        remote = remote.rstrip(".git")
        return f"{remote}/raw/main/{filename}"
    except Exception:
        return filename


def print_urls():
    """Print the raw URLs for all tracked files on startup."""
    print("\n  Raw GitHub URLs (use these in Claude chats):")
    for f in TRACKED_FILES:
        print(f"    {f}:")
        print(f"      {raw_url(f)}")
    print()


def main():
    watch_path = Path(WATCH_DIR)
    if not watch_path.exists():
        print(f"Error: WATCH_DIR does not exist: {WATCH_DIR}")
        print("Update WATCH_DIR at the top of this script.")
        sys.exit(1)

    if not (watch_path / ".git").exists():
        print(f"Error: {WATCH_DIR} is not a git repo.")
        print("Run: git init && git remote add origin <your-github-repo-url>")
        sys.exit(1)

    print(f"\n  Retro Guide Sync — watching {WATCH_DIR}")
    print(f"  Tracking {len(TRACKED_FILES)} files, debounce {DEBOUNCE_SECONDS}s")
    print_urls()
    print("  Waiting for file saves... (Ctrl+C to stop)\n")

    handler = GuideHandler()
    observer = Observer()
    observer.schedule(handler, str(watch_path), recursive=False)
    observer.start()

    try:
        while True:
            handler.flush_pending()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n  Stopped.")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
