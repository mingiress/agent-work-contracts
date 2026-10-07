"""Acceptance tests for the declared eight-skill publication inventory."""
import json
import pathlib
import runpy
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED = {
    "crew-contract", "goal-contract", "independent-review",
    "test-execution-and-reporting", "session-handover", "lesson-capture",
    "technical-decision-evaluation", "project-continuity",
}


class PackageAcceptance(unittest.TestCase):
    def test_exact_declared_skills_exist(self):
        paths = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in paths}, EXPECTED)
        for path in paths:
            self.assertGreater(len(path.read_text(encoding="utf-8")), 100)

    def test_declared_inventory_matches_validator(self):
        validator = runpy.run_path(str(ROOT / "scripts" / "validate.py"))
        self.assertEqual(validator["EXPECTED"], EXPECTED)

    def test_companion_provenance_matches_inventory(self):
        manifest = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
        self.assertEqual(set(manifest["companions"]["names"]), EXPECTED - {"crew-contract"})

    def test_standalone_companions_include_license(self):
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        for name in EXPECTED - {"crew-contract"}:
            with self.subTest(skill=name):
                path = ROOT / "skills" / name / "LICENSE"
                self.assertTrue(path.is_file(), "Individual installs need the license notice")
                self.assertEqual(path.read_text(encoding="utf-8"), license_text)


if __name__ == "__main__":
    unittest.main()
