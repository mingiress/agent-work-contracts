# Contributing

Keep every declared skill independently usable. Additions to this collection need a clear task boundary and a reason an existing skill cannot own the behavior; do not split one workflow into many mandatory fragments.

## Document contract

The generic companion entrypoints use JSON frontmatter between YAML `---` delimiters. JSON is a YAML-compatible subset and lets the standard-library validator parse their metadata without a YAML dependency. Include `name`, a concrete `Use when ...` description, `license: MIT`, and string-valued `metadata.author` and `metadata.version`. All metadata values must be strings under the [Agent Skills specification](https://agentskills.io/specification#metadata-field); encode tags as a comma-separated string, not an array. The vendored upstream keeps its original YAML and nested Hermes metadata extension unchanged.

Each companion needs explicit use/non-use conditions, a bounded workflow, an output contract, permission and stop boundaries, pitfalls, a verification checklist and one useful example. Supporting templates stay inside the same skill directory so an individual install remains usable. Optional references to other skills must not require the whole collection.

Write capabilities rather than invented CLI flags or universal slash commands. Label an example, expected output, actual observation and assumption distinctly. Avoid fixed providers/models, machine-specific paths, real internal domains, customer data, secrets or session logs. Do not add arbitrary installers, agent hooks, or automatic clipboard/configuration writes.

## Checks

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks this collection's metadata subset, required sections, local file links, known privacy/secret patterns and the upstream manifest. It is not a general-purpose YAML parser, comprehensive secret scanner, or behavioral proof. Use review for semantic scope, misleading claims and new privacy risks.

For a behavioral change, save actual no-target-skill and with-skill application observations before making an efficacy claim. A passing control is not a failure to invent away. Small smoke checks and fresh-context review are not causal benchmarks or cross-model independence. Keep private transcripts outside publication; share sanitized scenarios and honest limitations instead.

## Upstream

Follow [PROVENANCE.md](PROVENANCE.md). Changes to `crew-contract` belong upstream or in an explicitly attributed derivative, not hidden edits to the pinned subtree.

Use a scoped feature branch and an explicit file allowlist when staging. Review the actual final tree, run tests, and inspect staged content for credentials before publication. Never force-push or overwrite another contributor's working files.
