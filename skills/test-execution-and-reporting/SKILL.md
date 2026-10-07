---
{
  "name": "test-execution-and-reporting",
  "description": "Use when authorized tests or scenarios must be run and reported with evidence, distinct states, and explicit denominators.",
  "license": "MIT",
  "metadata": {
    "author": "Ming Fang",
    "version": "0.1.0",
    "tags": "testing, execution, evidence, reporting, status"
  }
}
---

# Test Execution and Reporting

## Overview
Report authorized checks against a known artifact and environment, distinguishing success, failure, blockage, and unattempted work. A report is evidence, not a correctness or release-readiness guarantee.

## When to Use
Use when repeatable checks need execution and evidence-based reporting.

Do not invent results, redesign an evaluation, secretly change code or data to obtain a pass, or claim readiness from test status alone. Never attribute stale results to an unknown revision. If execution is unauthorized or prerequisites are missing, report that limitation. Changes to implementation, fixtures, or evaluation require separate authorization.

## Workflow
1. **Pin context.** Record artifact/revision, environment/configuration, and run identifier. If identity is unknown, stop or mark blocked; never substitute stale results.
2. **Set scope and denominator.** Record planned cases and test/fixture source and version. State the total denominator. Note fixture provenance, assumptions, and validity gaps; unsuitable fixtures limit conclusions even when checks pass.
3. **Run as authorized.** Preserve exact commands/actions and parameters. Do not invisibly change code, data, fixtures, thresholds, or environment to obtain a pass. An approved change creates a distinct run.
4. **Record each case.** Capture expected and observed results plus evidence/blocker. Use **PASS** if evidence meets expectation; **FAIL** if not; **BLOCKED** if a named prerequisite prevents execution; **NOT_RUN** if unattempted. Never turn blocked/unrun into pass.
5. **Reconcile totals.** Count every planned case once. Show all four counts and denominators; they must sum to plan. Name percentage denominators; do not hide failures in an attempted-only rate.
6. **Preserve retests.** Tie each retest to its artifact/environment and changes. Keep earlier results; never overwrite a failure with a later pass.
7. **State limits.** Report untested areas, fixture limitations, and one authorized next step. A green result on one revision does not certify another or establish release readiness.

Use [`templates/report.md`](templates/report.md) to keep run identity, cases, totals, retests, and limitations together.

## Output Contract
Return artifact and environment; case and fixture identity/validity; exact commands; expected and observed per-case results with PASS/FAIL/BLOCKED/NOT_RUN; counts and planned denominator; retest history; limitations; and a safe next action. Never imply unrun tests passed. Do not claim release readiness without separate authorization and an appropriate broader decision.

## Common Pitfalls
- **Stale green result:** tie every observation to the artifact and environment actually tested.
- **Denominator drift:** report all planned cases; do not present only successful or attempted cases as the whole suite.
- **State collapse:** BLOCKED and NOT_RUN are not passes, and FAIL is not a blocker merely because it is inconvenient.
- **Invalid fixture:** a passing check on unsuitable test data may not answer the intended question; disclose validity limitations.
- **Pass-seeking edits:** covertly changing code, fixtures, thresholds, or data invalidates the comparison. Record authorized changes and rerun explicitly.
- **Retest erasure:** keep each run; say which revision changed and which result belongs to it.
- **Readiness overclaim:** tests provide scoped evidence, not a blanket approval or release decision.

## Verification Checklist
- [ ] Is the tested artifact and environment identified?
- [ ] Are test cases and fixture validity/provenance stated?
- [ ] Are exact commands/actions and expected outcomes preserved?
- [ ] Does every planned case have exactly one distinct state and evidence/blocker?
- [ ] Do PASS, FAIL, BLOCKED, and NOT_RUN counts sum to the stated denominator?
- [ ] Are any percentages accompanied by explicit denominator and counts?
- [ ] Are changes and retests linked without deleting prior observations?
- [ ] Are untested areas and release-readiness limits stated?

### Illustrative example
**Situation:** ten cases were planned on the current revision; four passed, one failed, two could not run because a required credential was unavailable, and three were never run.

**Report:** On the current revision, planned denominator 10: PASS 4/10, FAIL 1/10, BLOCKED 2/10, NOT_RUN 3/10. Four of ten planned cases passed (40%), not 80%; statuses reconcile and remain distinct. Capture exact environment, commands, case evidence, and credential blocker. Last week’s green CI is not evidence for this revision; partial results do not establish release readiness. Next: resolve the prerequisite, run blocked cases on this revision, and separately authorize any broader release decision. This example is illustrative, not a report of an executed run.
