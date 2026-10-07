"""Mutation fixtures prove the public-package guardrails fail closed."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        source = ROOT / "scripts" / "validate.py"
        self.assertTrue(source.is_file(), "Publication validator has not been implemented")
        spec = importlib.util.spec_from_file_location("publication_validator", source)
        assert spec is not None and spec.loader is not None
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "goal-contract"
        self.skill.mkdir(parents=True)

    def write_skill(self, *, name="goal-contract", description="Use when an objective needs observable acceptance.", body="## When to Use\n\nUse for unclear outcomes.\n\n## Workflow\n\nInspect evidence.\n\n## Output Contract\n\nRecord evidence and stop conditions.\n\n## Common Pitfalls\n\nDo not fabricate results.\n\n## Verification Checklist\n\nCheck current evidence.\n"):
        text = "---\n" + json.dumps({"name": name, "description": description, "license": "MIT", "metadata": {"version": "0.1.0", "author": "Ming Fang"}}) + "\n---\n\n" + body
        (self.skill / "SKILL.md").write_text(text, encoding="utf-8")

    def test_valid_standalone_skill(self):
        self.write_skill()
        self.assertEqual(self.module.validate_skill(self.skill, self.root), [])

    def test_rejects_name_directory_mismatch(self):
        self.write_skill(name="different-name")
        self.assertTrue(any("name" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_missing_supporting_file(self):
        self.write_skill(body="[Template](templates/missing.md)\n")
        self.assertTrue(any("link" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_link_outside_installed_skill(self):
        sibling = self.root / "README.md"
        sibling.write_text("root-only file", encoding="utf-8")
        self.write_skill(body="[Required guide](../../README.md)\n")
        self.assertTrue(any("outside" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_private_absolute_path(self):
        private_path = "/" + "Users" + "/" + "example" + "/workspace"
        self.write_skill(body="Evidence is at " + private_path + "\n")
        self.assertTrue(any("private" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_secret_looking_payload(self):
        payload = "gh" + "p_" + "A" * 36
        self.write_skill(body="Credential: " + payload)
        self.assertTrue(any("secret" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_oversized_description(self):
        self.write_skill(description="Use when " + "a" * 1100)
        self.assertTrue(any("description" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_non_string_metadata_values(self):
        self.write_skill()
        path = self.skill / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        meta = json.loads(parts[1])
        meta["metadata"]["tags"] = ["goals", "scope"]
        path.write_text("---\n" + json.dumps(meta) + "\n---" + parts[2], encoding="utf-8")
        self.assertTrue(any("metadata" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_malformed_frontmatter(self):
        (self.skill / "SKILL.md").write_text("---\n{broken JSON\n---\nbody\n", encoding="utf-8")
        self.assertTrue(any("frontmatter" in e for e in self.module.validate_skill(self.skill, self.root)))

    def test_rejects_private_data_in_eval_artifact(self):
        directory = self.root / "evals"
        directory.mkdir()
        private_path = "/" + "Users" + "/" + "example" + "/workspace"
        (directory / "cases.json").write_text(json.dumps({"path": private_path}), encoding="utf-8")
        errors = self.module.validate_repository(self.root)
        self.assertTrue(any("evals/cases.json" in e and "private" in e for e in errors))

    def test_upstream_hash_mismatch_is_detected(self):
        (self.skill / "SKILL.md").write_text("changed", encoding="utf-8")
        manifest = {"upstream": {"name": "goal-contract", "sha256": {"SKILL.md": "0" * 64}}}
        (self.root / "sources.json").write_text(json.dumps(manifest), encoding="utf-8")
        self.assertTrue(any("hash" in e for e in self.module.validate_upstream(self.root)))

    def test_unmanifested_upstream_file_is_detected(self):
        (self.skill / "SKILL.md").write_text("changed", encoding="utf-8")
        manifest = {"upstream": {"name": "goal-contract", "sha256": {}}}
        (self.root / "sources.json").write_text(json.dumps(manifest), encoding="utf-8")
        self.assertTrue(any("file set" in e for e in self.module.validate_upstream(self.root)))


if __name__ == "__main__":
    unittest.main()
