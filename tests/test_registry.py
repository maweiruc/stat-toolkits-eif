from pathlib import Path
import unittest

from eif_toolkit.registry_validation import (
    KEY_RE,
    load_registry,
    validate_registry,
)


REGISTRY = Path("examples/eif_formula_registry.yaml")


class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = load_registry(REGISTRY)

    def test_registry_passes_strict_validation(self):
        self.assertEqual(validate_registry(REGISTRY, strict=True), [])

    def test_entry_keys_are_snake_case(self):
        for key in self.registry:
            with self.subTest(key=key):
                self.assertRegex(key, KEY_RE)

    def test_entries_have_eif_or_status(self):
        for key, entry in self.registry.items():
            with self.subTest(key=key):
                self.assertTrue("eif" in entry or "status" in entry)

    def test_warnings_are_nonempty(self):
        for key, entry in self.registry.items():
            with self.subTest(key=key):
                warnings = entry.get("warnings")
                self.assertIsInstance(warnings, list)
                self.assertGreater(len(warnings), 0)

    def test_nonregular_entries_have_recommendation(self):
        for key, entry in self.registry.items():
            if "status" in entry and "eif" not in entry:
                with self.subTest(key=key):
                    self.assertIn("recommendation", entry)


if __name__ == "__main__":
    unittest.main()
