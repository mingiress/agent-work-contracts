---
{"name":"technical-decision-evaluation","description":"Use when a team must choose among technical approaches, defer a change, or retain the status quo under incomplete or contested evidence.","license":"MIT","metadata":{"author":"Ming Fang","version":"0.2.0","tags":"technical decisions, trade-offs, evidence, risk, reversibility"}}
---

# Technical Decision Evaluation

## When to Use

Use this method when a technical choice has plausible alternatives, uncertainty, or stakeholders with different priorities. It produces a bounded decision memo, not an exhaustive architecture study.

Do not use it for implementation planning, pure source research, or code review. It does not authorize architecture changes, implementation, spending, or operational risk. Identify missing decision ownership or permission; stop if either is decisive.

## Workflow

1. **Frame the choice.** State the decision question, desired outcome, owner, affected stakeholders, scope, constraints, deadline, and current authorization. Separate the choice from any follow-on work. Include the status quo unless unavailable.
2. **Compare feasible options.** Include realistic changes and relevant defer/wait or staged choices; apply the same criteria to each. Separate current observations from dated documents, stakeholder claims, inference, and unknowns; note sources and dates. An assigned upstream issue is not delivery, a commitment, or an ETA.
3. **Show consequences.** Compare one-time and ongoing costs, including migration, operations, support, people time, onboarding, and maintenance. Describe risks of acting and not acting, reversibility, lock-in, and rollback limits. Never invent ROI, units, probabilities, or precision. Cite measured/computed values and their basis; label bounded estimates and basis, or mark unknown.
4. **Test sensitivity.** Name decision-sensitive assumptions and the smallest check that could confirm or disprove each, with owner and permission status. If missing evidence could reverse the choice, pause for it rather than burying uncertainty in a confident verdict.
5. **Recommend conditionally.** State the preferred option under current facts, rationale, confidence, and what would change it. Set a review date or observable trigger, exit/rollback condition, escalation path, and accountable owner. If decisive evidence or authorization is missing, recommend a bounded hold and say what resolves it. A memo is not execution authorization.

Illustration: A working adapter passes a narrow local check, but onboarding burden is reported and migration effort and outage risk are unmeasured. An upstream issue is assigned without an ETA. Compare retaining the adapter, replacing it, and waiting; mark costs and timing unknown rather than inventing payback. A conditional memo may retain the adapter until scoped migration and outage evidence is reviewed with the service owner. It does not authorize migration.

## Output Contract

Use the linked [decision template](docs/template/decision.md). State question, outcome, scope, and owner; compare options with evidence quality; cover costs, risks, reversibility, and unknowns; list sensitive assumptions and a discriminating check; give a conditional recommendation and confidence; name revisit/exit/escalation conditions, owner, and next authorized action. Distinguish evidence from inference. Stop on missing decisive evidence or permission.

## Common Pitfalls

- Treating status quo as neutral: include its ongoing costs and risks.
- Treating an assigned ticket or roadmap item as delivery or a date: verify independently.
- Comparing full lifecycle costs with initial costs: include one-time and ongoing burdens for every option.
- Ignoring people who build, operate, support, or inherit the choice: include onboarding and maintenance.
- Inventing precise ROI or probabilities: source the calculation, label an estimate and basis, or mark unknown.
- Hiding assumptions behind an unconditional verdict: state the condition and check that could change it.
- Letting advice imply permission: identify the action authorized now and stop before unapproved execution.

## Verification Checklist

- Are the decision, owner, stakeholder outcome, scope, and permission explicit?
- Is status quo compared with realistic alternatives using consistent criteria?
- Are observations, historical claims, inference, assumptions, and unknowns distinguished and dated where possible?
- Are upstream assignment, delivery, and ETA kept distinct?
- Are one-time/ongoing and people costs, risks of action/inaction, and reversibility covered?
- Are numeric claims sourced or computed without unsupported precision?
- Are sensitive assumptions, discriminating check, conditional recommendation, confidence, revisit/exit/escalation, and owner present?
- Does the memo avoid authorizing work beyond current permission?
