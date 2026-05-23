"""Validate the EIF formula registry YAML file.

The validator checks registry structure and metadata only. It does not certify
that an EIF formula is mathematically correct.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


DEFAULT_REGISTRY = Path("examples/eif_formula_registry.yaml")

REQUIRED_FIELDS = {"observed_data", "target", "warnings"}
REGULAR_STRICT_FIELDS = {"eif", "estimator", "nuisances"}
NONREGULAR_STRICT_FIELDS = {"status", "recommendation"}
LIST_FIELDS = {"assumptions", "warnings"}
MAPPING_FIELDS = {"nuisances"}
STRING_FIELDS = {
    "observed_data",
    "target",
    "eif",
    "estimator",
    "status",
    "recommendation",
}

KEY_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_list_field(key: str, field: str, value: object) -> list[str]:
    if not isinstance(value, list) or not value:
        return [f"{key}: `{field}` must be a nonempty list"]
    if not all(is_nonempty_string(item) for item in value):
        return [f"{key}: `{field}` must contain only nonempty strings"]
    return []


def validate_entry(key: str, entry: object, *, strict: bool) -> list[str]:
    errors: list[str] = []

    if not KEY_RE.match(key):
        errors.append(f"{key}: key must be snake_case")

    if not isinstance(entry, dict):
        return errors + [f"{key}: entry must be a mapping"]

    missing = sorted(REQUIRED_FIELDS - entry.keys())
    for field in missing:
        errors.append(f"{key}: missing required field `{field}`")

    has_eif = "eif" in entry
    has_status = "status" in entry
    if not has_eif and not has_status:
        errors.append(f"{key}: must include either `eif` or `status`")

    for field in STRING_FIELDS:
        if field in entry and not is_nonempty_string(entry[field]):
            errors.append(f"{key}: `{field}` must be a nonempty string")

    for field in LIST_FIELDS:
        if field in entry:
            errors.extend(validate_list_field(key, field, entry[field]))

    for field in MAPPING_FIELDS:
        if field in entry and not isinstance(entry[field], dict):
            errors.append(f"{key}: `{field}` must be a mapping")

    if strict:
        if has_eif:
            for field in sorted(REGULAR_STRICT_FIELDS - entry.keys()):
                errors.append(f"{key}: strict mode missing `{field}`")
        elif has_status:
            for field in sorted(NONREGULAR_STRICT_FIELDS - entry.keys()):
                errors.append(f"{key}: strict mode missing `{field}`")

        if has_eif and has_status:
            errors.append(f"{key}: strict mode entries should not mix `eif` and `status`")

    return errors


def load_registry(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"{path}: registry must be a mapping")
    return data


def validate_registry(path: Path, *, strict: bool) -> list[str]:
    try:
        data = load_registry(path)
    except Exception as exc:  # pragma: no cover - CLI error path
        return [f"{path}: failed to parse YAML: {exc}"]

    errors: list[str] = []
    for key, entry in data.items():
        if str(key).startswith("_"):
            continue
        errors.extend(validate_entry(str(key), entry, strict=strict))
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default=str(DEFAULT_REGISTRY),
        help="Path to the EIF formula registry YAML file.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require regular entries to include estimator/nuisances and nonregular entries to include recommendation.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    path = Path(args.path)
    errors = validate_registry(path, strict=args.strict)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    mode = "strict" if args.strict else "default"
    print(f"OK: {path} passed {mode} validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
