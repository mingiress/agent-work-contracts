# Validation scope and observations

## Deterministic package checks

Run from a clean checkout:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These commands check the exact declared eight-skill inventory, companion frontmatter/metadata, required sections, local supporting links, known privacy/secret patterns, and the exact upstream file set and SHA-256 hashes. The tests include mutation fixtures for missing files, malformed frontmatter, wrong names, unsupported metadata values, oversized descriptions, escaping or broken links, private paths, secret-looking payloads and changed upstream content. This is not exhaustive security scanning or a general-purpose YAML parser.

The companion frontmatter is JSON, a valid YAML subset. The pinned flagship retains the original nested Hermes metadata extension; it is not represented as fully portable string-to-string metadata. A local YAML parser check can provide additional assurance, but the package validator intentionally has no third-party dependency.

## Initial-release application smoke checks

The [five pressure scenarios](evals/application-scenarios.json) cover unclear acceptance/permission, unavailable review artifacts, denominator manipulation, unverified handover claims and confounded root-cause learning.

The actual [baseline observations](evals/baseline-observations.json) contain five answers with twenty quoted check observations. All listed checks passed without loading the target companion files. No baseline behavioral gap was demonstrated, so this release does **not** claim that the skills improved compliance, reliability or cost.

The control inherited an agent system prompt and existing general instructions. It is contaminated, single-sample-per-case, and not blinded or a causal comparison. Author self-application is not independent review. A fresh-context reviewer exercises the with-skill application checks separately and checks actual documents, but this remains a smoke check, not a general efficacy study.

## Expansion 0.2 application smoke checks

The [two expansion scenarios](evals/v0.2-application-scenarios.json) cover decision pressure with missing migration/ETA evidence, and cold-start pickup with conflicting current-state declarations. Their [actual baseline observations](evals/v0.2-baseline-observations.json) contain two answers and eight quoted checks; all listed checks passed before target-file authoring. This demonstrates no behavioral deficit and supports no claim of improvement. The control inherits system instructions, uses one sample per case, and is not a blinded causal comparison. Any with-skill observations are application smoke checks, not proof of efficacy or cross-machine recovery.

The [with-skill observations](evals/v0.2-with-skill-observations.json) contain two actual hypothetical answers from a separate reviewer context; all eight listed checks were met, with literal supporting quotes. This remains single-sample application evidence, not proof of efficacy. Baseline answers and scores are preserved; three excerpts were expanded after review to cover the full statements being checked.

The [public-file pickup observation](evals/v0.2-pickup-observation.json) was **partial/blocked**: root README navigation identifies the package and its skills, but no authority for mutable active-project state. The reviewer reported that gap instead of inventing a current phase or creating another authority. This was a read-only exercise on available public files, not a fresh remote clone or cross-machine test; portability is not established.

## Independence and compatibility limits

- Producer and reviewer contexts are separate, but use the same configured model family. Shared model blind spots remain.
- No cross-harness execution or native install smoke test is claimed. The seven companions express generic capabilities; they do not add tools or guarantee permission enforcement, durable resume or reviewer isolation.
- Upstream scientific statements are attributed to the pinned source, not independently replicated here.
- Examples in the skills are illustrative and must never be reused as observed runtime evidence.
- Published CI verifies package integrity and unit fixtures; it does not exercise real external releases, production data, credentials or clipboard actions.

No installed user skill, user configuration or source repository is changed by building or publishing this collection. Installing the skills is a separate user action.
