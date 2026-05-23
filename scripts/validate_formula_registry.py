#!/usr/bin/env python3
"""CLI wrapper for EIF formula registry validation."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eif_toolkit.registry_validation import main


if __name__ == "__main__":
    raise SystemExit(main())
