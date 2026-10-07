---
{
  "name": "goal-contract",
  "description": "Use when a task goal is vague, underspecified, or delegated and needs an explicit outcome, scope, evidence, and acceptance contract.",
  "license": "MIT",
  "metadata": {
    "author": "Ming Fang",
    "version": "0.1.0",
    "tags": "goal, scope, evidence, acceptance, authority"
  }
}
---

# Goal Contract

## Overview
Turn a request into an agreement on the result, boundaries, evidence, and next safe move. It exposes ambiguity; it neither resolves unknowns nor grants authority.

## When to Use
Use when action or handoff depends on interpreting success, scope, proof, authority, or limits. It is useful for planning and delegated work.

Do not use it to execute work, silently rewrite a live goal, or infer permission from urgency or acceptance criteria. Keep clear low-risk requests lightweight. Surface conflicting direction and ask which goal is live.

## Workflow
1. **Name one outcome.** Phrase the intended result so a person can tell whether it exists. Separate the outcome from suggested means; ask a focused question when different interpretations change the result.
2. **Draw scope.** State what is included and excluded, plus any relevant artifact or revision. Do not let a convenient implementation choice expand scope.
3. **Separate evidence from assumptions.** Record observed facts with their source or artifact. Label estimates, expectations, missing inputs, and claims not independently checked as assumptions or unknowns.
4. **Make acceptance testable.** For every criterion, say what evidence would establish it. Do not promise evidence that is inaccessible; mark that criterion unresolved until evidence is available.
5. **State authority explicitly.** Distinguish approved actions from actions needing consent. A contract is descriptive, not an execution permit: drafting it never grants permission to act, access data, publish, or affect external systems.
6. **Set budget and stops.** Specify a time, attempt, or resource limit and conditions that require stopping or escalation, such as an absent artifact, conflicting instruction, unsafe side effect, or exceeded budget.
7. **Choose one safe next action.** It should advance clarification or gather authorized evidence, not cross a boundary. Present the contract for confirmation if approval is needed before execution.

Use the copyable form in [`templates/contract.md`](templates/contract.md). Keep the contract proportionate: a short task needs a short contract, but never omit a material authority or evidence gap.

## Output Contract
Return one outcome; included and excluded scope; facts distinguished from assumptions and unknowns; acceptance criteria paired with per-criterion proof; explicit authority; budget and stop conditions; and one immediate safe next action. Mark unresolved decisions and identify who must resolve them. Preserve the requester’s wording when a live goal is unclear; do not silently replace it with a more convenient objective.

An acceptance condition is not authority. If the contract cannot identify a safe action within granted permission, stop at clarification or read-only evidence gathering and state why. Do not describe a proposed action as completed or a missing proof as a pass.

## Common Pitfalls
- **Goal laundering:** changing “what” into an assumed “how.” Keep outcome separate from candidate approach.
- **Fact/assumption blending:** treat a confident report as a claim until its evidence is inspected.
- **Permission by implication:** urgency, a success metric, or a signed-looking contract does not grant missing authority.
- **Vague proof:** “works reliably” needs an observable threshold, representative evidence, and an identified denominator or time window where relevant.
- **Silent goal replacement:** when instructions conflict or change, expose the delta and seek resolution.
- **Open-ended effort:** a budget without a stop action is not a usable limit.

## Verification Checklist
- [ ] Is there exactly one stated outcome, and is it observable?
- [ ] Are scope and exclusions explicit enough to prevent silent expansion?
- [ ] Are evidence, assumptions, unknowns, and claims distinguished?
- [ ] Does each acceptance criterion name its own proof?
- [ ] Are approved actions separated from actions requiring consent?
- [ ] Are budget, stop conditions, and escalation explicit?
- [ ] Is the next action safe and within current authority?
- [ ] Were changes to a live goal surfaced rather than silently substituted?

### Illustrative example
**Request:** “Make the weekly export reliable and ship today”; no reliability threshold is supplied and a suggested fallback would upload data to a new service.

**Contract response:** Outcome: produce a weekly export meeting an agreed reliability threshold. Scope: inspect the current export and propose a measurable threshold; external upload is excluded. Evidence: threshold and current output are unavailable (unknowns, not facts). Acceptance: threshold agreed; a run on the current artifact demonstrates it, with the run evidence retained. Authority: clarification and authorized read-only inspection only; no upload or release permission. Budget: stop after 15 minutes or when evidence is unavailable. Safe next action: ask the requester to define the threshold and confirm whether any external transfer is permitted. This example is illustrative, not a report of an executed task.
