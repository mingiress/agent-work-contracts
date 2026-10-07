---
{
  "name": "session-handover",
  "description": "Use when work must continue across a session boundary or context handoff. Record verified state, uncertainty, permissions, and the next safe action.",
  "license": "MIT",
  "metadata": {
    "author": "Ming Fang",
    "version": "0.1.0",
    "tags": "handover, continuity, verification, scope"
  }
}
---
# Session Handover

## Overview
A session handover is a short-lived receipt for resuming work without treating narrative as evidence. Separate what is observable from a prior worker's report; identify the artifact or revision and give one safe next step. Capture it early and update material changes; do not copy a full conversation.

This bridges active sessions; it is not permanent project governance and does not replace an authoritative record or runbook. Do not overwrite those records. Link to them only when authorized and use an approved handover location.

## When to Use
Use this when context is about to be lost, work changes hands, or another operator must resume a task. Do not substitute it for project documentation, claim unsupported completion, grant access, or preserve sensitive data. If recipient, storage, or scope is unclear, ask or stop. Prior authorization does not prove current permission.

## Workflow
1. **Identify the work and boundary.** State the objective, owned scope, exclusions, and what kind of continuation is requested. Record the exact artifact location and revision, branch, change identifier, or equivalent identifier available. Preserve identifiers literally; do not normalize them.
2. **Capture live state.** Say what you inspected and when or against which revision. Separate observed facts from reports, unverified claims, and assumptions. Include uncommitted changes, running work, pending operations, and failures. Mark possibly stale details as unknown.
3. **Protect information and authority.** Never include credential contents or verification codes. If relevant, note only that a credential is required and use approved secret handling. Keep content appropriate to its storage location. The recipient must confirm current authorization before acting.
4. **Choose one next action.** Give one actionable step, its evidence target, and a stop condition. Identify what to verify first, especially for live state or external effects. Name missing input or the decision-maker; do not disguise a blocker as a plan.
5. **Save and transfer safely.** Use the template; save only where authorized without replacing authoritative material. The recipient must revalidate state before execution: this is a snapshot, not a live guarantee.

## Output Contract
A handover states objective/scope, exact artifact and revision, observed facts, separate claims and assumptions, pending work, permission boundaries, and one next action. Mark unavailable facts unknown. Omit secret values entirely. Keep it brief but actionable.

**Illustrative example:** “Export fix; scope is the local parser change only. Last inspected revision `fix/export-v2`; its test run failed. A worker says the fix is complete, but I have not inspected the resulting artifact. Token access is reportedly configured; no token value is recorded. No external upload is authorized. Next: inspect the current diff and rerun the failing test on the exact revision; stop if the branch or permission boundary differs. Recipient: recheck the live revision and current authorization before acting.” This example demonstrates structure, not evidence about any real project.

## Common Pitfalls
- Reporting another worker's completion claim as a verified fact; label the source and inspect the artifact.
- Saying “current” without a revision or inspection point; identify what was actually observed.
- Treating old permission as transferable; have the recipient validate current authority.
- Including secrets “for convenience”; record their presence or requirement without their contents.
- Writing a durable process history into a handover; link to the proper project record instead.
- Listing many vague tasks; choose one immediate next action and a clear stop condition.

## Verification Checklist
- [ ] Objective, owned scope, and exclusions are clear.
- [ ] Exact artifact/revision and observed state are distinguished from claims and assumptions.
- [ ] Uncommitted changes and running work are noted or explicitly unknown.
- [ ] No credential contents or unauthorized private material are present.
- [ ] Storage is approved; no authoritative project document is overwritten.
- [ ] One next action and stop condition are stated.
- [ ] Recipient is told to revalidate live state and authorization before execution.

Use [`templates/handover.md`](templates/handover.md) for a self-contained fill-in form.
