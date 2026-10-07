---
{
  "name": "independent-review",
  "description": "Use when a material artifact or decision needs a read-only check by someone other than its producer against pinned evidence.",
  "license": "MIT",
  "metadata": {
    "author": "Ming Fang",
    "version": "0.1.0",
    "tags": "independent review, artifact, evidence, findings, read-only"
  }
}
---

# Independent Review

## Overview
Review the actual artifact and evidence, not the producer’s description of intended work. This workflow separates producing from evaluating, anchors the review to a specific version, and makes unavailable evidence visible. A review is an assessment, not a change, approval, or release authorization.

## When to Use
Use for a consequential artifact, result, or decision where a separate read-only perspective could find correctness, safety, completeness, or evidence gaps. The review should have a stated question and criteria.

Do not use self-review as an independent review, or review a narrative in place of the artifact when the artifact is material to the conclusion. If the artifact, its identity, or decisive evidence is unavailable, return BLOCKED rather than clean. Do not edit, publish, deploy, or approve through this workflow. For a trivial, directly checkable change, a proportionate direct check may suffice; do not manufacture a review gate.

## Workflow
1. **Establish separation.** Confirm the reviewer did not produce the artifact or its key claims in the same context. Disclose any overlap or constraint; do not call self-review independent.
2. **Pin what is reviewed.** Identify the exact artifact and revision (for example, a content digest, immutable version, or stable identifier). If it changes during review, stop and request a new review of the new version.
3. **Collect actual evidence.** Inspect source artifacts and relevant observed results. Distinguish inspected evidence from the producer’s summary, inference, and unavailable inputs. Do not treat “all checks passed” as proof without the corresponding output and context.
4. **Apply criteria.** Check the requested scope and material risks. Prefer deterministic checks or primary evidence where available. A finding must be actionable and anchored: state severity, location, impact, evidence, and remedy. Separate confirmed findings from questions or uncertainty.
5. **Return a bounded verdict.** Use REVIEWED only when the pinned artifact and necessary evidence were available; use BLOCKED when not. State material findings or “no material findings,” plus residual uncertainty and unreviewed areas. Neither verdict approves, deploys, or publishes the artifact.
6. **Leave the artifact unchanged.** Return findings to the responsible owner. They decide whether to change or authorize anything; after a material change, review that new pinned artifact rather than carrying the old verdict forward.

Use [`templates/review.md`](templates/review.md) to capture the identity, evidence, verdict, findings, and limits. Review depth should match the risk and the evidence that can actually be inspected.

## Output Contract
Return the reviewer’s separation status; artifact identity/revision; evidence actually inspected; review question and criteria; verdict (REVIEWED or BLOCKED); material findings with **severity, location, impact, evidence, and remedy**; residual uncertainty; and one safe next action. “No material findings” means only that none were found within the stated scope and evidence. It is not approval, release readiness, deployment permission, or proof that uninspected properties are correct.

## Common Pitfalls
- **Reviewing a summary:** ask for the real artifact and the evidence needed to evaluate it.
- **Unpinned review:** name the exact revision; re-review a changed artifact.
- **Self-review by another label:** context separation and producer/reviewer separation matter; disclose overlap.
- **Blocked disguised as clean:** missing decisive evidence prevents a clean verdict.
- **Unanchored findings:** identify a location and evidence, explain impact, and offer a remedy; label uncertainty.
- **Approval creep:** a review does not confer authority to edit, publish, release, or deploy.

## Verification Checklist
- [ ] Is the reviewer distinct from the producer and key claims’ authoring context?
- [ ] Is the actual artifact pinned to an identifiable revision?
- [ ] Were evidence and producer assertions clearly distinguished?
- [ ] Were review criteria and scope stated?
- [ ] Are findings complete, evidence-anchored, and actionable?
- [ ] Is missing evidence labeled BLOCKED, not clean?
- [ ] Does the verdict explicitly avoid approval or deployment claims?
- [ ] Is the artifact unchanged and the next action within authority?

### Illustrative example
**Situation:** a producer asks for approval in two minutes, but supplies only a prose summary; the diff and test output are unavailable, and the reviewer helped implement the change in this same context.

**Review response:** Verdict: **BLOCKED — independent review not performed.** Artifact identity: unavailable; no diff or revision supplied. Evidence inspected: producer’s prose summary only, which is not evidence of the actual change or test results. Separation: not independent because reviewer participated in implementation in this context. Findings about correctness: none can be established from available material; this is not “no material findings.” Safe next action: request the immutable artifact revision and relevant observed test output, then assign a distinct reviewer. No edits, publication, or approval. This example is illustrative, not a report of an executed review.
