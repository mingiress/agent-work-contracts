---
{
  "name": "project-continuity",
  "description": "Use when a sustained project must be resumed without prior chat and its active objective, status, blockers, or next authorized action need evidence-based confirmation.",
  "license": "MIT",
  "metadata": {
    "author": "Ming Fang",
    "version": "0.2.0",
    "tags": "project continuity, cold start, current state, evidence"
  }
}
---
# Project Continuity

Resume sustained work from project artifacts, not chat memory. Find the existing startup route and current-state authority first. Live evidence may reveal stale status; preserve conflicts for authorized reconciliation.

## When to Use
Use when resuming a sustained project without prior chat to recover its objective, status, blockers, and safe next action. Not for one-off handover, global memory, repository governance, or cleanup. Follow project conventions; do not impose a filename, path, harness, or authority.

## Workflow
1. **Discover.** Read startup/navigation instructions and follow them to one existing current-state authority. If none is discoverable, report the gap; do not create a parallel record or prescribe a location.
2. **Separate roles.** Stable instructions cover enduring policy/navigation; current state declares mutable work; historical evidence records past decisions/results; temporary handover transfers near-term context. Link these roles; do not substitute one for another or overwrite instructions with changing status.
3. **Check evidence.** Within authority, inspect relevant artifacts and exact revisions. Status declares intended work; source, tests, or changed artifacts may contradict it. Never let documentation overrule direct evidence. Report both claims and sources as partial/blocked; seek authorized reconciliation before updating or proceeding.
4. **Bound the record.** Include objective/phase; exact revision/artifacts; status, verification evidence and unknowns; blockers/decision ceiling; owner; one next authorized action and stop conditions; source links. Mark unsupported fields unknown. The linked template is a checklist, not a required file or location.
5. **Respect boundaries.** Update existing state only with applicable approval. Do not automatically alter protected instructions, configuration, ignore rules, or permissions. Exclude sensitive contents and secrets. Ignored machine-local state is not cross-machine recovery.
6. **Drill cold start.** Give a fresh read-only recipient only the repository root; let them follow its existing route without the expected answer. They must identify authority, status, blocker, and next action from actual artifacts, citing evidence. Missing/conflicting proof is partial/blocked. Claim portability only if approved shared/versioned state is available to the recipient and the drill succeeds there; a file or commit alone is insufficient.

## Output Contract
Report startup route and one authority; objective/phase; exact revision/artifacts or unknowns; declared status separate from live facts; evidence/unknowns; blocker, owner, decision ceiling; one next authorized action and stop condition; sources; and drill result (passed, partial, or blocked). No portability claim without recipient availability and a successful drill.

**Illustrative example:** “The startup guide leads to the existing status record. It says the export change is complete at `r17`; the live checkout is `r18` and its focused test fails. Completion at `r18` is unverified; test output is direct evidence and the record is stale. Owner: unknown. Decision ceiling: inspect/report only. Blocker: conflict, no reconciliation approval. Next: ask the authorized owner to reconcile the record against `r18` and its test; stop before edits. Cold-start: partial.” Details are fictional.

## Common Pitfalls
- Creating a second status file; follow the documented route or report that no authority is discoverable.
- Treating “complete” as proof; check live artifacts and tests.
- Letting documentation erase contradictory direct evidence; preserve conflict for authorized reconciliation.
- Confusing history or handover with current status; link them, keep roles distinct.
- Assuming ignored state or a commit is portable; verify recipient access and drill.
- Treating read-only access as permission to edit protected files or expose sensitive data.

## Verification Checklist
- [ ] Followed startup instructions to one existing authority, or recorded the discovery gap.
- [ ] Separated stable instructions, current status, history, and handover.
- [ ] Checked live evidence; preserved conflicts and marked unknowns.
- [ ] Included bounded fields, owner, next authorized action, stop condition, and sources.
- [ ] Made no unapproved protected/configuration/ignore/permission changes; omitted sensitive contents.
- [ ] Ran an unprompted, read-only drill on actual artifacts; missing/conflicting proof is partial/blocked.
- [ ] Claimed portability only after approved shared/versioned availability and successful recipient drill.

Use [`templates/current-state.md`](templates/current-state.md) as a checklist, not authorization to create a new state file.