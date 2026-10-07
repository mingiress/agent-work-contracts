"""Acceptance tests: publication must contain exactly six usable skills."""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED = {
    "crew-contract", "goal-contract", "independent-review",
    "test-execution-and-reporting", "session-handover", "lesson-capture",
}


class PackageAcceptance(unittest.TestCase):
    def test_exact_six_skills_exist(self):
        paths = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in paths}, EXPECTED)
        for path in paths:
            self.assertGreater(len(path.read_text(encoding="utf-8")), 100)


if __name__ == "__main__":
    unittest.main()
