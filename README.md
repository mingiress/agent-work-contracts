# Agent Work Contracts

**Eight skills for bounded, evidence-bearing agent work: compare approaches, define the task, divide ownership, review and verify the result, hand it over, preserve project continuity, and capture what was learned.**

This collection combines an unchanged, pinned [crew-contract](https://github.com/mfang0126/crew-contract) flagship with seven newly written generic companion skills. It is a set of procedure documents—not a multi-agent runtime, permission system, or promise of autonomous correctness.

## Pick the skill you need

| Skill | Use it when | Boundary |
|---|---|---|
| [crew-contract](skills/crew-contract/SKILL.md) | Work benefits from bounded delegation and independent review | Role, ownership, evidence and orchestration contracts |
| [goal-contract](skills/goal-contract/SKILL.md) | An objective is vague, autonomous, or at risk of scope drift | One outcome, observable acceptance, budget and stop conditions |
| [independent-review](skills/independent-review/SKILL.md) | A material result needs fresh-context scrutiny before acceptance | Frozen artifact review; the reviewer does not edit or publish |
| [test-execution-and-reporting](skills/test-execution-and-reporting/SKILL.md) | Tests need actual execution and an honest report | Pass, fail, blocked and not-run remain distinct |
| [session-handover](skills/session-handover/SKILL.md) | Work must survive a session, agent or context transition | Current-state receipt plus receiving-agent revalidation |
| [lesson-capture](skills/lesson-capture/SKILL.md) | A correction or verified failure should improve future work | Evidence-backed learning stored at the narrowest useful level |
| [technical-decision-evaluation](skills/technical-decision-evaluation/SKILL.md) | Competing technical approaches need an evidence-backed choice | Conditional recommendation, costs, reversibility and revisit triggers; not permission to implement |
| [project-continuity](skills/project-continuity/SKILL.md) | A sustained project must be resumed without prior chat | Existing current-state authority, startup path and a read-only pickup drill; not a second handover log |

Use one independently, or combine them:

**Decision → goal → delegation → independent review → verification → handover → continuity → learning.**

For code, tests often run before review; the arrow is a responsibility map, not a mandatory execution order. Simple tasks stay simple: no forced fan-out, no review ceremony for a trivial explanation, and no whole-collection loading requirement.

## Install

### Hermes Agent

Add this repository as a skill tap, then inspect and install only what you want:

```bash
hermes skills tap add mingiress/agent-work-contracts
hermes skills search goal-contract
hermes skills install mingiress/agent-work-contracts/goal-contract
```

Alternatively, clone the repository and copy one **whole skill directory**, including its templates/references, into your profile's skill directory. Check for name conflicts first; do not overwrite a customized local skill. Reload skills in an existing session after installation.

See [Hermes's skill-tap documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#publishing-a-custom-skill-tap). A repository publication alone does not install anything in your runtime.

### Other Agent Skills-compatible tools

Use the tool's documented skill-directory mechanism and point it at, or copy, a selected directory under `skills/`. Preserve the complete directory. The seven companions use valid JSON-as-YAML frontmatter and tool-neutral capability descriptions. Do not paste every skill into a permanent system prompt, replace a project's instruction file, or assume that these documents add slash commands.

The flagship retains an optional Hermes-specific reference. Platform adapters and cross-harness execution have not been tested for this release. Generic instructions do not guarantee that a particular harness supports isolated reviewers, durable resume or identical permission semantics.

## Try it

Ask your agent to read `goal-contract` and produce a task contract for:

> Make an existing CSV export preserve leading-zero identifiers. Work only on the export path and its regression test. No new dependencies or external data uploads. Stop if the format requirement is ambiguous.

Then use `independent-review` on the actual final diff and current test results—not the author's completion summary. Follow each skill's own template and stop boundaries. Their examples are illustrative, not execution evidence.

## Verify the package

Python 3.9+; standard library only:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The guardrails check metadata, the exact declared eight-skill set, required sections, local supporting links, known privacy/secret patterns and SHA-256 integrity of the upstream copy. They do not establish behavioral efficacy, exhaustive secret detection, or cross-platform compatibility. See [VALIDATION.md](VALIDATION.md) for executed checks and limitations.

## Provenance and license

`crew-contract` comes from **mfang0126/crew-contract**, pinned at `b7d045cb09d746cdf9780a2e03d8f151da76c75d`, with the original MIT notice preserved. Its upstream version remains 1.4.0. This collection's version is 0.2.0 (initial version 0.1.0); the companion versions are recorded separately. The original five remain at 0.1.0; the two new skills start at 0.2.0.

Read [PROVENANCE.md](PROVENANCE.md) and [sources.json](sources.json) for the source boundary and exact imported-file hashes. The seven companions are new generic documents, not exports of private project material.

[MIT license](LICENSE) · [Contribution guide](CONTRIBUTING.md)
