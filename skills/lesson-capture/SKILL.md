---
{
  "name": "lesson-capture",
  "description": "Use when a mistake, recovery, or repeated outcome may yield a useful lesson. Separate evidence from hypotheses and route the bounded lesson appropriately.",
  "license": "MIT",
  "metadata": {
    "author": "Ming Fang",
    "version": "0.1.0",
    "tags": "lessons, learning, verification, scope"
  }
}
---
# Lesson Capture

## Overview
A lesson records an observed outcome and what it supports changing next time. Capture it after a failure, recovery, or repeated result. Keep causal claims proportional to evidence: the outcome may be real while its explanation remains uncertain. A lesson is not permission to change state or universal policy.

## When to Use
Use this when a workflow failure or recovery may prevent recurrence. Do not turn speculation, personal preference, or an unisolated correlation into a rule. Do not write to project logs, skills, memory, or other stores without permission. If destination or authority is unclear, draft only where authorized or stop.

## Workflow
1. **Describe the trigger and observed error.** Record context, action, concrete outcome, and how it was detected. Include enough to recognize the situation without secrets or irrelevant transcripts. Distinguish observation from report.
2. **Classify the cause.** Mark root cause confirmed only when evidence isolates or directly establishes it. Otherwise state “hypothesis” and list plausible alternatives or confounders. Several changes before success do not identify which change caused it. Do not upgrade confidence because an explanation sounds plausible or a deadline is near.
3. **State a bounded correction.** Write a procedure that applies only to the observed conditions. Include what to check, what action to take, and when to stop or escalate. Describe what real verification was run and its result; if none, say “not verified” and name the smallest discriminating check. Never invent a test, counterexample search, or successful outcome.
4. **Set scope and expiry.** State affected project/workflow, known version or context limits, and when to review or expire the lesson (for example, after a dependency or process change). Before promoting a tentative lesson to a reusable method, search for counterexamples or supporting observations from meaningfully different cases. Keep contrary evidence and limits visible.
5. **Route before writing.** Put project-specific outcomes in an authorized project log. Put reusable procedures in the existing owning skill or guidance; avoid duplicate owners. A stable user preference may go to applicable memory only when relevant and authorized. Otherwise keep a draft. Obtain permission before persistent writes and verify any saved result.

## Output Contract
A lesson entry records trigger, observed outcome, cause status/evidence, bounded correction, real verification (or its absence), applicability and expiry, and destination. Minimize private details. Do not change persistent state without authorization. Keep hypotheses labeled until evidence changes their status.

**Illustrative example:** “Trigger: a dependency install failed, then succeeded after registry selection, network retry, and cache bypass. Observed result: success after all three changes. Cause: hypothesis—cache behavior may have contributed; not isolated. Correction: for this project, record the original error and test one change at a time on the next recurrence; do not disable caching globally. Verification: none separates these causes yet; compare a cache-enabled retry with other variables held constant. Scope: this project and current dependency setup; review after configuration changes. Route: draft for the project log if its owner approves; no permanent change now.” The example is illustrative, not a claim about a real system.

## Common Pitfalls
- Mistaking “after” for “because of”; mark confounded causes as hypotheses.
- Writing an attractive explanation as policy before checking counterexamples.
- Claiming verification from a report or imagined test; record only actual checks.
- Making a broad fix from narrow evidence; state boundaries and expiry.
- Routing project detail into generic guidance or duplicating an existing skill's ownership.
- Treating lesson capture as automatic memory; secure permission before every state write.

## Verification Checklist
- [ ] Trigger and observed error/result are concrete and attributed correctly.
- [ ] Root cause is labeled confirmed or hypothesis with supporting evidence.
- [ ] Correction is bounded, actionable, and has a stop/escalation rule.
- [ ] Verification is real and reported accurately, or explicitly marked absent.
- [ ] Scope, exclusions, and expiry/review condition are stated.
- [ ] Counterexamples are checked before promotion beyond the observed case.
- [ ] Destination follows lesson type and established ownership.
- [ ] Persistent write is authorized; saved effect is read back where applicable.

Use [`templates/lesson.md`](templates/lesson.md) as a fill-in entry.
