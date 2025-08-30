"""Helpers for resolving resource paths in dev and PyInstaller onefile builds."""

from __future__ import annotations

import sys
from pathlib import Path


def base_path() -> Path:
    """Return the base path for bundled resources.

    In a PyInstaller onefile build, resources are unpacked to sys._MEIPASS.
    In dev, it's the project root (parent of the app package).
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    # Fall back to repo root assuming this file is at app/utils/paths.py
    return Path(__file__).resolve().parents[2]


def asset_path(relative: str) -> Path:
    """Resolve a path inside the assets directory.

    Example: asset_path("book.ico")
    """
    # Try standard locations
    for cand in (
        base_path() / "app" / "assets" / relative,
        base_path() / "assets" / relative,
    ):
        if cand.exists():
            return cand
    # Return first candidate even if missing; caller can handle absence
    return base_path() / "app" / "assets" / relative
