#!/usr/bin/env python3
"""Validate this six-skill collection without third-party dependencies.

Companion frontmatter uses JSON, a YAML-compatible subset. The unchanged
upstream YAML is checked for required scalars and against its pinned hashes;
this is deliberately not a general-purpose YAML or secret parser.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

EXPECTED = {
    "crew-contract", "goal-contract", "independent-review",
    "test-execution-and-reporting", "session-handover", "lesson-capture",
}
REQUIRED_HEADINGS = (
    "When to Use", "Workflow", "Output Contract", "Common Pitfalls",
    "Verification Checklist",
)
SECRET_PATTERNS = (
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    re.compile(
        "-----" + "BEGIN " + "(?:RSA |EC |OPENSSH )?" + "PRIVATE KEY" + "-----"
    ),
)
PRIVATE_PATTERNS = (
    re.compile(r"/(?:Users|home)/[^/\s]+/"),
    re.compile(r"\b(?:iress(?:-wealth)?\.atlassian\.net|wealth-dev-au|APE-\d+)\b", re.I),
)
LINKS = re.compile(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")


def text_errors(text, label):
    errors = []
    if any(p.search(text) for p in SECRET_PATTERNS):
        errors.append(f"{label}: possible secret payload (value not printed)")
    if any(p.search(text) for p in PRIVATE_PATTERNS):
        errors.append(f"{label}: private path or internal identifier")
    return errors


def frontmatter(text, upstream=False):
    if not text.startswith("---\n"):
        raise ValueError("frontmatter must start at byte zero")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter closing delimiter missing")
    header, body = text[4:end], text[end + 5:]
    if upstream:
        result = {}
        for field in ("name", "description", "license"):
            match = re.search(rf"^{field}:\s*(.+)$", header, re.M)
            if match:
                value = match.group(1).strip()
                result[field] = json.loads(value) if value.startswith('"') else value
    else:
        result = json.loads(header)
        if not isinstance(result, dict):
            raise ValueError("frontmatter must be a mapping")
    return result, body


def validate_skill(skill_dir, root):
    skill_dir, root = Path(skill_dir), Path(root)
    errors = []
    label = skill_dir.name
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        return [f"{label}: SKILL.md missing"]
    try:
        text = path.read_text(encoding="utf-8")
        meta, body = frontmatter(text, upstream=label == "crew-contract")
    except (ValueError, OSError) as exc:
        return [f"{label}: invalid frontmatter: {exc}"]
    name, description = meta.get("name"), meta.get("description")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != label:
        errors.append(f"{label}: name must match directory and the skill-name format")
    if not isinstance(description, str) or not description or len(description) > 1024:
        errors.append(f"{label}: description must contain 1..1024 characters")
    if not body.strip() or len(text) > 100_000:
        errors.append(f"{label}: empty body or size limit exceeded")
    if meta.get("license") != "MIT":
        errors.append(f"{label}: MIT license marker missing")
    if label != "crew-contract":
        metadata = meta.get("metadata", {})
        if not isinstance(metadata, dict) or not metadata.get("author") or not metadata.get("version"):
            errors.append(f"{label}: author/version metadata missing")
        if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
            errors.append(f"{label}: metadata must map string keys to string values")
        for heading in REQUIRED_HEADINGS:
            if not re.search(rf"^## {re.escape(heading)}\s*$", body, re.M):
                errors.append(f"{label}: required heading missing: {heading}")
        if not isinstance(description, str) or not description.startswith("Use when "):
            errors.append(f"{label}: description must state a Use when trigger")
    for file in sorted(skill_dir.rglob("*")):
        if file.is_symlink():
            errors.append(f"{label}: symlink not allowed: {file.name}")
            continue
        if not file.is_file():
            continue
        if file.name.startswith(".env") or file.suffix.lower() in {".pem", ".key", ".p12"}:
            errors.append(f"{label}: credential file not allowed: {file.name}")
        try:
            content = file.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"{label}: non-text or unreadable supporting file: {file.name}")
            continue
        errors.extend(text_errors(content, f"{label}/{file.relative_to(skill_dir)}"))
        if file.suffix != ".md":
            continue
        for target in LINKS.findall(content):
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"} or not parsed.path:
                continue
            if parsed.scheme:
                errors.append(f"{label}: unsupported link scheme: {target}")
                continue
            destination = (file.parent / unquote(parsed.path)).resolve()
            try:
                destination.relative_to(skill_dir.resolve())
            except ValueError:
                errors.append(f"{label}: supporting link points outside installed skill: {target}")
                continue
            if not destination.exists():
                errors.append(f"{label}: broken supporting link: {target}")
    return errors


def validate_upstream(root):
    root = Path(root)
    try:
        manifest = json.loads((root / "sources.json").read_text(encoding="utf-8"))["upstream"]
        name, hashes = manifest["name"], manifest["sha256"]
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]+", name) or not isinstance(hashes, dict):
            raise ValueError("invalid upstream manifest shape")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"upstream manifest invalid: {exc}"]
    base = root / "skills" / name
    actual = {str(p.relative_to(base)) for p in base.rglob("*") if p.is_file()}
    errors = []
    if actual != set(hashes):
        errors.append("upstream file set differs from pinned manifest")
    for rel, expected in hashes.items():
        path = base / rel
        try:
            path.resolve().relative_to(base.resolve())
        except ValueError:
            errors.append("upstream manifest path escapes skill directory")
            continue
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append(f"upstream hash mismatch: {rel}")
    return errors


def validate_repository(root):
    root = Path(root)
    paths = sorted((root / "skills").glob("*/SKILL.md"))
    errors = []
    if {p.parent.name for p in paths} != EXPECTED:
        errors.append("package must contain exactly the six declared skills")
    for path in paths:
        errors.extend(validate_skill(path.parent, root))
    errors.extend(validate_upstream(root))
    # Published examples and CI metadata must not bypass the skill scanner.
    for directory in (root / "evals", root / ".github"):
        for file in sorted(directory.rglob("*")):
            if file.is_symlink():
                errors.append(f"{file.relative_to(root)}: symlink not allowed")
            elif file.is_file():
                try:
                    errors.extend(text_errors(file.read_text(encoding="utf-8"), str(file.relative_to(root))))
                except (UnicodeError, OSError):
                    errors.append(f"{file.relative_to(root)}: unreadable publication artifact")
    for file in sorted(root.glob("*.md")):
        content = file.read_text(encoding="utf-8")
        errors.extend(text_errors(content, file.name))
        for target in LINKS.findall(content):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            destination = (root / unquote(parsed.path)).resolve()
            try:
                destination.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{file.name}: link escapes repository")
                continue
            if not destination.exists():
                errors.append(f"{file.name}: broken local link: {target}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skill", help="Validate one skill, useful during authoring")
    args = parser.parse_args(argv)
    if args.skill:
        if args.skill not in EXPECTED:
            parser.error("--skill must be one of the six declared names")
        errors = validate_skill(args.root / "skills" / args.skill, args.root)
    else:
        errors = validate_repository(args.root)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS:", args.skill or "six skills, supporting links, privacy patterns and pinned upstream hashes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
